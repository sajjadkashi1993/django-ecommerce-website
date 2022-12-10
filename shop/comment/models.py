from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel
from product.models import Product

User = get_user_model()


class Comment(BaseModel):
    """ 
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
                             related_name='comments', verbose_name=_('User'), null=True, blank=True)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('product'), related_name='comments')

    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,verbose_name=_('parent'), null=True, blank=True)

    nickname = models.CharField(_('nickname'), max_length=100, blank=True, null=True)
    email = models.EmailField(_('email'), max_length=100, blank=True, null=True)
    rate = models.IntegerField(_('rate'), choices=RATE.choices, default=RATE.GOOD)

    status = models.IntegerField(_('status'), 
        choices=STATUS.choices, default=STATUS.PENDING)

    body = models.TextField(verbose_name=_('Comment'))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.body
