from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from shuup.admin.base import AdminModule, MenuEntry
from shuup.admin.menu import CONTACTS_MENU_CATEGORY
from shuup.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from example.first.models import Customer


class ExampleFirstAdminModule(AdminModule):
    name = _("Manage Customer")
    breadcrumbs_menu_entry = MenuEntry(name, "shuup_admin:example.first.customer.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^example-first/customer",
            view_template="example.first.admin_module.customer.Customer%sView",
            name_template="example.first.customer.%s"
        )

    def get_menu_entries(self, request):

        return [
            MenuEntry(
                text=_("Manage Customers"),
                icon="fa fa-file-text",
                url="shuup_admin:example.first.customer.list",
                category=CONTACTS_MENU_CATEGORY,
                ordering=-1,
                aliases=[_("Manage Customers")]
            )
        ]

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Customer, "shuup_admin:example.first.customer", object, kind)
