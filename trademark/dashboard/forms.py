from django import forms
from django.forms import models as modelforms
from django.forms.formsets import formset_factory
from django.db.models import Q, get_model


Brand = get_model('trademark', 'Brand')


class TrademarkForm(forms.ModelForm):

    class Meta:
        model = get_model('trademark', 'Trademark')
        exclude = ('slug', 'opening_periods', )
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }

    def clean_reference(self):
        ref = self.cleaned_data['reference']
        if ref == "":
            return None
        return ref


# class BrandForm(forms.ModelForm):

#     class Meta:
#         model = Brand


# class BrandFormset(modelforms.BaseInlineFormSet):
#     extra = 10
#     can_order = False
#     can_delete = True
#     max_num = 30 # Reasonably safe number of maximum period intervals per day
#     absolute_max = 30
#     model = Brand
#     fk = 'id'
#     validate_max = True

#     def form(self, *args, **kwargs):
#         form = BrandForm(*args, **kwargs)
#         return form



# class BrandInline(object):
#     def __init__(self, model, request, instance, kwargs=None, view=None):
#         self.data = request.POST
#         self.instance = instance

#     def construct_formset(self):
#         return BrandFormset(
#             self.data or None,
#             self.instance,
#         )
