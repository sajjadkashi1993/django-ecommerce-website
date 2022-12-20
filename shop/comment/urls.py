from django.urls import path
from .views import CreateCommentView

app_name = 'comment'
urlpatterns = [
    path('create/<int:pk>/', CreateCommentView.as_view(), name='create_comment'),
]
