from django import forms
from django.forms import models as modelforms
from django.forms.formsets import formset_factory
from django.utils.translation import ugettext_lazy as _, ugettext
from django.db.models import Q, get_model


class BrandForm(forms.ModelForm):

    class Meta:
        # exclude = ('description', )
        model = get_model('brand', 'Brand')


class DashboardBrandSearchForm(forms.Form):
    name = forms.CharField(label=_('Brand name'), required=False)
    # address = forms.CharField(label=_('Address'), required=False)

    def is_empty(self):
        d = getattr(self, 'cleaned_data', {})
        empty = lambda key: not d.get(key, None)
        return empty('name') and empty('address')

    def apply_address_filter(self, qs, value):
        words = value.replace(',', ' ').split()
        q = [Q(address__search_text__icontains=word) for word in words]
        return qs.filter(*q)

    def apply_name_filter(self, qs, value):
        return qs.filter(name__icontains=value)

    def apply_filters(self, qs):
        for key, value in self.cleaned_data.items():
            if value:
                qs = getattr(self, 'apply_%s_filter' % key)(qs, value)
        return qs
