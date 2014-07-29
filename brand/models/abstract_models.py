# -*- coding: utf-8 -*-
from django.db import models
from oscar.models.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from .fields import FormulaField


class AbstractBrand(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = AutoSlugField(_('Slug'), max_length=100, unique=True, populate_from='name')
    description = models.TextField(_('Description'), null=True, blank=True)
    formula = FormulaField(_('Formula'), null=True, blank=True, max_length=100)
    country = models.ForeignKey('address.Country', verbose_name=_("Country"))

    def __unicode__(self):
        return self.name

    def calc_price(self, price):
        data = {'price': price}

        if self.formula == "" or self.formula is None:
            return price

        try:
            code = compile(self.formula, '', 'eval')
            calced_price = eval(code, {}, data)
        except:
            raise Exception('Wong formula')

        return calced_price

    class Meta:
        ordering = ('name',)
        abstract = True
