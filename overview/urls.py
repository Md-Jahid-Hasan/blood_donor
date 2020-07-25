from django.conf.urls import url
from .views import get_data, get_chart, make_donate_month

urlpatterns = [
    url(r'^a/$', get_data, name='get_data'),
    url(r'', get_chart, name='get_chart'),
    url(r'^data/$', make_donate_month, name="make_donate_month"),
]