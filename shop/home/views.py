from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.core.mail import send_mail
from order.models import OrderItem

from product.models import Product
from django.db.models import Count

from .forms import ContactForm


class ContactUsView(View):
    form_class = ContactForm
    template_name = 'contact-us.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = cd['name'] + '\n' + \
                cd['comment'] + '\nemail:' + cd['email']
            try:
                send_mail('contact us', message, 'sajjad.kashi29@gmail.com',
                          ['sajjad.kashi29@gmail.com'])
                messages.success(request, 'Your comment sended', 'success')
            except:
                messages.error(
                    request, 'Unfortunately, your comment was not sent', 'danger')

        return render(request, self.template_name, {'form': form})


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        best_selling_id = OrderItem.objects.filter(order__status__gt=2).values(
            'product').annotate(count=Count('product')).order_by('-count')
        best_selling = []
        for item in best_selling_id:
            product = Product.undeleted_objects.get(id=item['product'])
            best_selling.append(product)
        return render(request, self.template_name, context={'best_selling': best_selling})
