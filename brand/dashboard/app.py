from django.conf.urls import patterns, url

from oscar.core.application import Application
from oscar.views.decorators import staff_member_required

from brand.dashboard import views


class TrademarksDashboardApplication(Application):
    name = 'brand-dashboard'

    brand_list_view = views.BrandListView
    brand_create_view = views.BrandCreateView
    brand_update_view = views.BrandUpdateView
    brand_delete_view = views.BrandDeleteView

    def get_urls(self):
        urlpatterns = patterns('',
            url(
                r'^$',
                self.brand_list_view.as_view(),
                name='brand-list'
            ),
            url(
                r'^create/$',
                self.brand_create_view.as_view(),
                name='brand-create'
            ),
            url(
                r'^update/(?P<pk>[\d]+)/$',
                self.brand_update_view.as_view(),
                name='brand-update'
            ),
            url(
                r'^delete/(?P<pk>[\d]+)/$',
                self.brand_delete_view.as_view(),
                name='brand-delete'
            ),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = TrademarksDashboardApplication()
