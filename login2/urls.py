from django.conf.urls import url
from django.contrib import admin
from login2app import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index,name='index'),
    url(r'^intro/$', views.intro,name='intro'),
    url(r'^industry/$', views.industry,name='indus'),
    url(r'^grow/$', views.grow,name='grow'),
    url(r'^train/$', views.train,name='train'),
    url(r'^marketing/$', views.marketing,name='market'),
    url(r'^shop/$', views.shop,name='shop'),
    url(r'^member/$', views.member,name='member'),
    url(r'^register/$', views.register,name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^base/$', views.base),
]