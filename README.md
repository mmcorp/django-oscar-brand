Trademarks for django oscar
======================

Features
--------

Installation
------------

If running with Oscar, add an additional path to your `TEMPLATE_DIRS`:
``` python
from trademarks import TEMPLATE_DIR as TRADEMARKS_TEMPLATE_DIR

TEMPLATE_DIRS = (
    ...
    TRADEMARKS_TEMPLATE_DIR)
```

This allows the templates to be customised by overriding blocks instead of
replacing the entire template.

In order to make the trademarks accessible via the Oscar dashboard you need to append it to your `OSCAR_DASHBOARD_NAVIGATION`
``` python
from oscar.defaults import *
from django.utils.translation import ugettext_lazy as _

OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': _('Trademarks'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Trademarks'),
                'url_name': 'trademark:trademark-list',
            },
            {
                'label': _('Brands'),
                'url_name': 'trademark:trademark-brand-list',
            },
        ]
    })
```

API
---

Error handling
--------------

Contributing
------------

Settings
--------