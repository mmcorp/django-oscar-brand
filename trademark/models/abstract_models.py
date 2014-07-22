# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .fields import FormulaField


class AbstractTrademark(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)

    class Meta:
        abstract = True


class AbstractBrand(models.Model):
    trademark = models.ForeignKey('trademark.Trademark', verbose_name=_("Trademark"),
                                  related_name='brands')
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)
    product_class = models.ForeignKey('catalogue.ProductClass', verbose_name=_("Product class"),
                                      related_name='brands')
    formula = FormulaField(_('Formula'), null=True, blank=True, max_length=100)

    class Meta:
        abstract = True
