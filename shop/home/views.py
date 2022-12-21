from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact-us.html')

    def post(self, requst):
        print(33333333333333333, requst.POST)
        # TODO mail contact us
        return JsonResponse({'message': 'Your message has been successfully sent', 'status': 'success'})
