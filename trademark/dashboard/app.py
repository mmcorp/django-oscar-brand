from django.conf.urls import patterns, url

from oscar.core.application import Application
from oscar.views.decorators import staff_member_required

from trademark.dashboard import views


class TrademarksDashboardApplication(Application):
    name = 'trademarks-dashboard'

    trademark_list_view = views.TrademarkListView
    trademark_create_view = views.TrademarkCreateView
    trademark_update_view = views.TrademarkUpdateView
    trademark_delete_view = views.TrademarkDeleteView

    brand_list_view = views.BrandListView
    brand_create_view = views.BrandCreateView
    brand_update_view = views.BrandUpdateView
    brand_delete_view = views.BrandDeleteView

    def get_urls(self):
        urlpatterns = patterns('',
            url(
                r'^$',
                self.trademark_list_view.as_view(),
                name='trademark-list'
            ),
            url(
                r'^create/$',
                self.trademark_create_view.as_view(),
                name='trademark-create'
            ),
            url(
                r'^update/(?P<pk>[\d]+)/$',
                self.trademark_update_view.as_view(),
                name='trademark-update'
            ),
            url(
                r'^delete/(?P<pk>[\d]+)/$',
                self.trademark_delete_view.as_view(),
                name='trademark-delete'
            ),
            url(
                r'^brands/$',
                self.brand_list_view.as_view(),
                name='brand-list'
            ),
            url(
                r'^brands/create/$',
                self.brand_create_view.as_view(),
                name='brand-create'
            ),
            url(
                r'^brands/update/(?P<pk>[\d]+)/$',
                self.brand_update_view.as_view(),
                name='brand-update'
            ),
            url(
                r'^brands/delete/(?P<pk>[\d]+)/$',
                self.brand_delete_view.as_view(),
                name='brand-delete'
            ),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = TrademarksDashboardApplication()
