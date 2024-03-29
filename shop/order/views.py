import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

from .models import Order
from .helper import OrderHelper
from django.conf import settings


class ChackOutView(LoginRequiredMixin, View):
    template_name = 'order/checkout.html'

    def get(self, request):
        return render(request, self.template_name)


class OrderVerifyView(LoginRequiredMixin, View):
    def get(self, request):
        order_id = request.session['order_pay']['order_id']
        order = Order.objects.get(id=int(order_id))
        # t_status = request.GET.get('Status')
        # t_authority = request.GET['Authority']
        if request.GET.get('Status') == 'OK':
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req_data = {
                "merchant_id": settings.MERCHANT,
                "amount": float(order.grand),
                # "authority": t_authority
            }
            # req = requests.post(url=ZP_API_VERIFY, data=json.dumps(
            #     req_data), headers=req_header)
            # if len(req.json()['errors']) == 0:
            #     t_status = req.json()['data']['code']
            if True:
                t_status = 100

                if t_status == 100:
                    order_helper = OrderHelper(order)
                    order_helper.operation_after_payment(request)
                    return render(request, 'order/order.html', {'order': order})
                    # return HttpResponse('Transaction success.\nRefID: ' + str(
                    #     req.json()['data']['ref_id']
                    # ))
                # elif t_status == 101:
                #     return HttpResponse('Transaction submitted : ' + str(
                #         req.json()['data']['message']
                #     ))
                # else:
                #     return HttpResponse('Transaction failed.\nStatus: ' + str(
                #         req.json()['data']['message']
                #     ))
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        else:
            return render(request, 'order/order.html', {'error': 'Payment was not successful'})
