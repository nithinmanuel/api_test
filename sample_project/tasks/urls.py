from django.conf.urls import url
from tasks import views
urlpatterns = [
    url(r'^neos/$',views.neo_list),
    url(r'^neos/(?P<pk>[0-9]+)$',views.neo_detail),]






