from decimal import Decimal
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.api.serializers import CartSerilizer
from ..utils import check_discount


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
