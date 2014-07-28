from django.conf.urls import patterns, url

from oscar.core.application import Application

from brand import views


class BrandApplication(Application):
    name = 'brand'
    list_view = views.ListView
    detail_view = views.DetailView

    def get_urls(self):
        urlpatterns = super(BrandApplication, self).get_urls()
        urlpatterns += patterns('',
            url(r'^$', self.list_view.as_view(),
                name='index'),
            url(r'^(?P<dummyslug>[\w-]+)/(?P<pk>\d+)/$',
                self.detail_view.as_view(), name='detail'),
        )
        return self.post_process_urls(urlpatterns)


application = BrandApplication()
