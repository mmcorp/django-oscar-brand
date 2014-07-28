from django.views import generic
from django.db.models import get_model
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _, ugettext
from extra_views import (CreateWithInlinesView, UpdateWithInlinesView,
                         InlineFormSet)
from trademark.dashboard import forms


Trademark = get_model('trademark', 'Trademark')
Brand = get_model('trademark', 'Brand')


class BrandInline(InlineFormSet):
    model = Brand
    form_class = forms.BrandInlineForm
    extra = 10


class TrademarkEditMixin(object):
    # Common model to operate with
    model = Trademark

    # Common form constructed by model fields
    form_class = forms.TrademarkForm

    # Update/create template
    template_name = "trademark/dashboard/trademark_update.html"

    # After save go to
    success_url = reverse_lazy('trademarks-dashboard:trademark-list')

    # Additional forms
    inlines = [BrandInline, ]


class TrademarkCreateView(TrademarkEditMixin, CreateWithInlinesView):

    def get_context_data(self, **kwargs):
        ctx = super(TrademarkCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Create new trademark")
        return ctx


class TrademarkUpdateView(TrademarkEditMixin, UpdateWithInlinesView):

    def get_context_data(self, **kwargs):
        ctx = super(TrademarkUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx


class TrademarkDeleteView(generic.DeleteView):
    model = Trademark
    template_name = "trademark/dashboard/trademark_delete.html"
    success_url = reverse_lazy('trademarks-dashboard:trademark-list')


class TrademarkListView(generic.ListView):
    model = Trademark
    template_name = "trademark/dashboard/trademark_list.html"
    context_object_name = "trademark_list"
    paginate_by = 20
    filterform_class = forms.DashboardTrademarkSearchForm

    def get_title(self):
        data = getattr(self.filterform, 'cleaned_data', {})

        name = data.get('name', None)

        if name:
            return ugettext('Trademarks matching "%s"') % (name)
        else:
            return ugettext('Trademarks')

    def get_context_data(self, **kwargs):
        data = super(TrademarkListView, self).get_context_data(**kwargs)
        data['filterform'] = self.filterform
        data['queryset_description'] = self.get_title()
        return data

    def get_queryset(self):
        qs = self.model.objects.all()
        self.filterform = self.filterform_class(self.request.GET)
        if self.filterform.is_valid():
            qs = self.filterform.apply_filters(qs)
        return qs


class BrandEditMixin(object):
    # Common model to operate with
    model = Brand

    # Common form constructed by model fields
    form_class = forms.BrandForm

    # After save go to
    success_url = reverse_lazy('trademarks-dashboard:brand-list')


class BrandDeleteView(generic.DeleteView):
    model = Brand
    template_name = "trademark/dashboard/brand_delete.html"
    success_url = reverse_lazy('trademarks-dashboard:brand-list')


class BrandListView(generic.ListView):
    model = Brand
    template_name = "trademark/dashboard/brand_list.html"
    context_object_name = "brand_list"
    paginate_by = 20
    filterform_class = forms.DashboardBrandSearchForm

    def get_title(self):
        data = getattr(self.filterform, 'cleaned_data', {})

        name = data.get('name', None)

        if name:
            return ugettext('Brands matching "%s"') % (name)
        else:
            return ugettext('Brands')

    def get_context_data(self, **kwargs):
        data = super(BrandListView, self).get_context_data(**kwargs)
        data['filterform'] = self.filterform
        data['queryset_description'] = self.get_title()
        return data

    def get_queryset(self):
        qs = self.model.objects.all()
        self.filterform = self.filterform_class(self.request.GET)
        if self.filterform.is_valid():
            qs = self.filterform.apply_filters(qs)
        return qs


class BrandCreateView(BrandEditMixin, generic.CreateView):
    template_name = "trademark/dashboard/brand_update.html"
    context_object_name = "brand_list"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        ctx = super(BrandCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Create new brand")
        return ctx


class BrandUpdateView(BrandEditMixin, generic.UpdateView):
    template_name = "trademark/dashboard/brand_update.html"
    context_object_name = "brand_list"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        ctx = super(BrandUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx
