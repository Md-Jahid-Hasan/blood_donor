from django.conf.urls import url
from .views import get_data, get_chart

urlpatterns = [
    url(r'^a/$', get_data, name='get_data'),
    url(r'', get_chart, name='get_chart'),

]