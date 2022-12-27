from rest_framework import serializers
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'parent', 'is_reply', 'nickname', 'email', 'rate', 'status', 'body')

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Comment.objects.create(product_id=product_id,**validated_data) 


