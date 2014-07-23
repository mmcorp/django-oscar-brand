Trademarks for django oscar
======================

`ПОДРЕДАКТИРОВАТЬ И ПЕРЕВЕСТИ`

Основная идея этого модуля заключается в автоматическом расчете цен на товары по формуле исходя из "дороговизны" бренда. Не секрет, что на рынке существует множество товаров заменителей. Часть из которых по техническим характеристикам одинакова. Но цена на такие товары различается. Можно с увереностью сказать, что престижность "бренда" повышает стоимость товаров.

Набросок к описанию:

Trademark - это некая марка, компания-производитель и агрегатор брендов

Brand - это узкая линейка товаров

Например применимо к производителю (марке) Apple можно выделить следующие бренды: iphone, macbook pro, time machine и т.п.


Features
--------

`ПОДРЕДАКТИРОВАТЬ И ПЕРЕВЕСТИ`

Появление такой сущности как Марка и Бренд дают возможность группировать товары с целью разделения логики формирования цены, а также предоставляют возможность создания фильтров для удобного ориентирования клиента в представленных линейках товаров.

Возможности, наиболее наглядные:
* Создание фильтров на основе Брендов (соотв. создание landing pages)
* Расчет надбавочной стоимости товаров исходя из популярности марок и брендов
* Товары представлены брендами имеющими описание, что повышает лояльность пользователей.
* И т.п. Вы можете продолжить список сами

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
