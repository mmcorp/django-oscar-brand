from django.conf.urls import patterns, url

from oscar.core.application import Application

from trademark import views


class TrademarksApplication(Application):
    name = 'trademark'
    list_view = views.TrademarkListView
    detail_view = views.TrademarkDetailView
    brand_detail_view = views.BrandDetailView

    def get_urls(self):
        urlpatterns = super(TrademarksApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^$', self.list_view.as_view(),
                name='index'),
            url(r'^(?P<dummyslug>[\w-]+)/(?P<pk>\d+)/$',
                self.detail_view.as_view(), name='detail'),
            url(r'^brand/(?P<dummyslug>[\w-]+)/(?P<pk>\d+)/$',
                self.brand_detail_view.as_view(), name='brand_detail'),
        )
        return self.post_process_urls(urlpatterns)


application = TrademarksApplication()