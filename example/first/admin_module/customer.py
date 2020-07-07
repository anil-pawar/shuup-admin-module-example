from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from shuup.admin.utils.picotable import Column
from shuup.admin.utils.views import CreateOrUpdateView, PicotableListView
from example.first.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "shop",
            "first_name",
            "last_name",
        ]


class CustomerEditView(CreateOrUpdateView):
    model = Customer
    template_name = "admin/customer.jinja"
    form_class = CustomerForm
    context_object_name = "customer"
    add_form_errors_as_messages = True


class CustomerListView(PicotableListView):
    url_identifier = "example.first.customer"
    model = Customer

    default_columns = [
        Column("id", _("Id")),
        Column("shop", _("Shop")),
        Column("first_name", _("First Name")),
        Column("last_name", _("Last Name")),
        Column("identifier", _("Unique Code")),
        Column("created_at", _("Created On")),
        Column("modified_at", _("Updated On")),
    ]
