from django.conf.urls import url
from .views import add_donor_details, search_donor, donor_list, donor_details

urlpatterns = [
    url(r'^update_details/$', add_donor_details, name='add_donor_details'),
    url(r'^$', search_donor, name='search_donor'),
    url(r'^donor/list/$', donor_list, name='donor_list'),
    url(r'^donor/details/(?P<pk>\d+)/$', donor_details, name='donor_details')
]