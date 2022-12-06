from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
# Create your models here.
# from accounts.models import User
# from comments.managers import CommentManager
from core.models import BaseModel

User = get_user_model()


class Comment(BaseModel):
    """ Comment model

        This is a model for comments.

    """

    class RATE(models.IntegerChoices):
        """
            This is a class for rating choices.
        """
        VERY_BAD = 1, _('Very bad')
        BAD = 2, _('Bad')
        GOOD = 3, _('Good')
        VERY_GOOD = 4, _('Very good')
        EXCELLENT = 5, _('Excellent')

    class STATUS(models.IntegerChoices):
        """
            This is a class for status choices.
        """
        PENDING = 1, _('Pending')
        APPROVED = 2, _('Approved')
        REJECTED = 3, _('Rejected')

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             related_name='comments', verbose_name=_('User'),null=True, blank=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    rate = models.IntegerField(choices=RATE.choices, default=RATE.GOOD)
    # content_type = models.ForeignKey(
        # ContentType, on_delete=models.CASCADE, related_name='comments')
    status = models.IntegerField(
        choices=STATUS.choices, default=STATUS.PENDING)
    object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(verbose_name=_('Comment'))

    # objects = CommentManager()

    def __str__(self):
        return self.user.email
