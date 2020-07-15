from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.create_user, name='signup'),
    url(r'^logout/$', views.user_logout, name='logout'),
]