from django.db import models


# Re-use Oscar's trademark model
class AbstractTrademark(models.Model):
    name = models.CharField(_('Name'), max_length=100, unique=True)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)
    product_class = models.ForeignKey('catalogue.ProductClass', verbose_name=_("Product class"),
                                      related_name='brands')

    class Meta:
        abstract = True
