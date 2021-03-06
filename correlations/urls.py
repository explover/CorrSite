from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<tissue_id>[0-9]+)/runs/$', views.runs, name='runs'),
    url(r'^(?P<tissue_id>[0-9]+)/image/$', views.get_image, name='get_image'),
    url(r'^get_tracks$', views.get_tracks, name="get_tracks"),
    url(r'^got_tracks$', views.got_tracks, name="got_tracks"),
    url(r'^runs$', views.runs, name='runs') 
]
