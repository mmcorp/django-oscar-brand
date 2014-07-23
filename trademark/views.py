from django.views import generic
from django.db.models import get_model
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# from trademark.forms import TrademarkSearchForm
# from trademark.utils import get_geographic_srid, get_geodetic_srid

Trademark = get_model('trademark', 'trademark')
Brand = get_model('trademark', 'brand')


class TrademarkListView(generic.ListView):
    model = Trademark
    template_name = 'trademark/list.html'
    context_object_name = 'trademark_list'


class TrademarkDetailView(generic.DetailView):
    model = Trademark
    template_name = 'trademark/detail.html'
    context_object_name = 'trademark'


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = 'trademark/brand/detail.html'
    context_object_name = 'brand'
