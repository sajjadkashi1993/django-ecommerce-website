from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from .forms import CommentForm
from product.models import Product

class CreateCommentView(View):

    def post(self, request,**kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            product = Product.undeleted_objects.get(pk=kwargs['pk'])
            new_comment.product = product
            if request. user.is_authenticated:
                new_comment.user = request.user
            new_comment.save()
            return JsonResponse({'msg': 'Your comment send'}, status=201)
        return JsonResponse(form.errors, status=200)