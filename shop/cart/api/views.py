from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from ..models import CartItem, Cart
from product.models import Product
from .serializers import CartSerilizer

class AddToCart(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            cart = user.carts.get_or_create(user=user,status=2)[0]
            product = Product.undeleted_objects.get(id=request.POST['product'])
            try:
                cart_item =CartItem.objects.create(cart=cart,product=product,quantity=request.POST['quantity'])
            except IntegrityError:
                cart_item =CartItem.objects.get(cart=cart,product=product)
                cart_item.quantity=request.POST['quantity']
                cart_item.save()
            return Response(CartSerilizer(cart).data, status=status.HTTP_201_CREATED)
        else:
            # request.session.clear()
            try:
                request.session['cart'][request.POST['product']]=request.POST['quantity']
                request.session.modified = True
            except KeyError:
                request.session['cart'] = {request.POST['product']:request.POST['quantity']}
            return Response( request.session['cart'], status=status.HTTP_201_CREATED)


class DelCart(APIView):
    def delete(self, request):
        if request.user.is_authenticated:
            user = request.user
            cart = user.carts.get_or_create(user=user,status=2)[0]
            product = Product.undeleted_objects.get(id=request.POST['product'])
            cart_item =CartItem.objects.get(cart=cart,product=product)
            cart_item.delete()
            return Response(CartSerilizer(cart).data, status=status.HTTP_204_NO_CONTENT)
        else:
            # request.session.clear()
            try:
                request.session['cart'][request.POST['product']]=request.POST['quantity']
                request.session.modified = True
            except KeyError:
                request.session['cart'] = {request.POST['product']:request.POST['quantity']}
            return Response( request.session['cart'], status=status.HTTP_201_CREATED)


class ShowCart(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            cart = user.carts.get_or_create(user=user,status=2)[0]
            serilizer = CartSerilizer(cart)
            return Response(serilizer.data, status=status.HTTP_200_OK)


