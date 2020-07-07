from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from shuup.core.models import Product
from django.contrib.auth.models import User


class Customer(models.Model):
    shop = models.ForeignKey("shuup.Shop", verbose_name=_("shop"), related_name="customer_shop")
    identifier = models.CharField(max_length=200, blank=False, verbose_name=_("Unique Identifier"), unique=True)
    first_name = models.CharField(max_length=200, blank=False, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=200, blank=False, verbose_name=_("Last Name"))
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True, verbose_name=_("created at"))
    modified_at = models.DateTimeField(auto_now=True, editable=False, db_index=True, verbose_name=_("modified at"))
    modified_by = models.ForeignKey(User, default=1)

    def __str__(self):
        return self.identifier
