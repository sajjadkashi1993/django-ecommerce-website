from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ChackOutView(LoginRequiredMixin, View):
    template_name='order/checkout.html'
    def get(self,request):
        return render(request, self.template_name)