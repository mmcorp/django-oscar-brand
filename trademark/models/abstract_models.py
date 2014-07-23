# -*- coding: utf-8 -*-
from django.db import models
from oscar.models.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from .fields import FormulaField


class AbstractTrademark(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = AutoSlugField(_('Slug'), max_length=100, unique=True, populate_from='name')
    description = models.TextField(_('Description'), null=True, blank=True)
    country = models.ForeignKey('address.Country', verbose_name=_("Country"))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        abstract = True


class AbstractBrand(models.Model):
    trademark = models.ForeignKey('trademark.Trademark', verbose_name=_("Trademark"),
                                  related_name='brands')
    name = models.CharField(_('Name'), max_length=100, unique=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    slug = AutoSlugField(_('Slug'), max_length=100, unique=True, populate_from='name')
    product_class = models.ManyToManyField('catalogue.ProductClass', verbose_name=_("Product class"),
                                           related_name='brands')
    formula = FormulaField(_('Formula'), null=True, blank=True, max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        abstract = True
