from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.message_list, name='message_list'),
    url(r'^api/mark_read$', views.mark_read, name='message_id'),
    url(r'^False$', views.mark_all_not_read, name='message_id'),
]
