from decimal import Decimal
import json
import requests
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.api.serializers import CartSerilizer
from discount.models import Coupon
from order.exceptions import QuantityOrderException
from ..utils import check_discount
from accounts.api.serializers import AddressSerilizers
from ..models import Order
from .serializers import OrderSerilizers
from ..helper import OrderHelper
from django.db import transaction


class CheckOutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        cart = user.carts.get_or_create(user=user, status=2)[0]
        serialized_card = CartSerilizer(cart)
        tax = round(serialized_card.data.get('grand_total') * Decimal(0.09), 2)
        coupon_code = request.GET.get('coupon')
        amount = serialized_card['grand_total'].value
        discount, data = check_discount(request, coupon_code, amount)
        shipping = 10
        grand_total = serialized_card.data.get('grand_total')
        total = grand_total + tax + Decimal(shipping - discount)

        data.update({
            'cart': serialized_card.data,
            'tax': tax,
            'discount': discount,
            'shipping': shipping,
            'total': total
        })
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = request.user
        cart = user.carts.get_or_create(user=user, status=2)[0]
        data = {
            'user': user.id,
            'country': request.POST.get('country'),
            'province': request.POST.get('province'),
            'city': request.POST.get('city'),
            'address': request.POST.get('address'),
            'postal_code': request.POST.get('postal_code')
        }
        address = AddressSerilizers(data=data)
        # if address.is_valid():
        #     address.save()
        # else:
        #     return Response({'errors':address.errors})

        coupon_code = request.POST.get('coupon')

        try:
            coupon = Coupon.objects.get(code=coupon_code).pk
        except:
            coupon = None

        serialized_card = CartSerilizer(cart)
        tax = round(serialized_card.data.get('grand_total') * Decimal(0.09), 2)
        amount = serialized_card['grand_total'].value
        discount = check_discount(request, coupon_code, amount)[0]
        shipping = 10
        sub_total = serialized_card.data.get('grand_total')
        total = sub_total + tax + Decimal(shipping)
        grand = total - Decimal(discount)

        data.update({
            'coupon': coupon,
            'sub_total': sub_total,
            'tax': tax,
            'shipping': shipping,
            'total': total,
            'discount': discount,
            'grand': grand,
            'receiver_name': request.POST.get('receiver_name'),
            'receiver_mobile': request.POST.get('receiver_mobile'),
            'content': request.POST.get('content'),
        })
        try:
            with transaction.atomic():
                order_serializer = OrderSerilizers(data=data)
                if order_serializer.is_valid():
                    order = order_serializer.save()
                else:
                    return Response({'errors': order_serializer.errors})
                order_helper = OrderHelper(order)
                order_helper.add_order_items(cart)
        except QuantityOrderException as e:
            return Response({'errors': str(e)})
        # if not order_helper.check_order()[0]:
        #     return Response({'errors':  order_helper.check_order()[1]})
        return Response({'order_id': order.pk})


MERCHANT = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
CallbackURL = 'http://127.0.0.1:8000/orders/verify/'


class OrderPayView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        request.session['order_pay'] = {
            'order_id': order.id,
        }
        req_data = {
            "merchant_id": MERCHANT,
            "amount": float(order.grand),
            "callback_url": CallbackURL,
            "description": description,
            # "metadata": {"mobile": request.user.phone_number, "email": request.user.email}
        }
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
            req_data), headers=req_header)
        # TODO logging req.json()

        # if len(req.json()['errors']) == 0:
        if True:
            # authority = req.json()['data']['authority']
            # return Response({'redirect': ZP_API_STARTPAY.format(authority=authority)})
            return Response({'redirect': 'http://127.0.0.1:8000/order/order-pay/'})
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return Response({"Error code": e_code, "Error Message": e_message})
