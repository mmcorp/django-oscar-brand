from django.views import generic
from django.db.models import get_model
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _, ugettext
from extra_views import (CreateWithInlinesView, UpdateWithInlinesView,
                         InlineFormSet)
from trademark.dashboard import forms


Trademark = get_model('trademark', 'Trademark')
Brand = get_model('trademark', 'Brand')


class TrademarkEditMixin(object):
    pass
    # inlines = [forms.BrandInline, ]


class TrademarkCreateView(TrademarkEditMixin, CreateWithInlinesView):
    model = Trademark
    template_name = "trademark/dashboard/trademark_update.html"
    form_class = forms.TrademarkForm
    success_url = reverse_lazy('trademarks-dashboard:trademark-list')


class TrademarkUpdateView(TrademarkEditMixin, UpdateWithInlinesView):
    model = Trademark
    template_name = "trademark/dashboard/trademark_update.html"
    form_class = forms.TrademarkForm
    success_url = reverse_lazy('trademarks-dashboard:trademark-list')

    def get_context_data(self, **kwargs):
        ctx = super(TrademarkUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx


class TrademarkDeleteView(generic.ListView):
    model = Trademark
    template_name = "trademark/dashboard/trademark_list.html"
    context_object_name = "trademark_list"


class TrademarkListView(generic.ListView):
    model = Trademark
    template_name = "trademark/dashboard/trademark_list.html"
    context_object_name = "trademark_list"
    paginate_by = 20
    # filterform_class = forms.DashboardTrademarkSearchForm

    # def get_title(self):
    #     data = getattr(self.filterform, 'cleaned_data', {})

    #     name = data.get('name', None)
    #     address = data.get('address', None)

    #     if name and not address:
    #         return ugettext('Trademarks matching "%s"') % (name)
    #     elif name and address:
    #         return ugettext('Trademarks matching "%s" near "%s"') % (name, address)
    #     elif address:
    #         return ugettext('Trademarks near "%s"') % (address)
    #     else:
    #         return ugettext('Trademarks')

    # def get_context_data(self, **kwargs):
    #     data = super(TrademarkListView, self).get_context_data(**kwargs)
    #     data['filterform'] = self.filterform
    #     data['queryset_description'] = self.get_title()
    #     return data

    # def get_queryset(self):
    #     qs = self.model.objects.all()
    #     self.filterform = self.filterform_class(self.request.GET)
    #     if self.filterform.is_valid():
    #         qs = self.filterform.apply_filters(qs)
    #     return qs
