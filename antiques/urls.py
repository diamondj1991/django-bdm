from django.conf.urls import url

from . import views

app_name = 'antiques'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.CategoryIndexView.as_view(), name='category_index'),
    url(r'^category/(?P<pk>[0-9]+)/type/(?P<type_id>[0-9]+)$', views.TypeDetail.as_view(), name='type_detail')
]
