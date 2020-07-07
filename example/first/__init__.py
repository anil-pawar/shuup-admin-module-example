from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = __name__
    verbose_name = _("Example First")
    label = "example_first"

    provides = {
        "admin_module": [
            "example.first.admin_module:ExampleFirstAdminModule",
        ],
    }

default_app_config = __name__ + ".AppConfig"
