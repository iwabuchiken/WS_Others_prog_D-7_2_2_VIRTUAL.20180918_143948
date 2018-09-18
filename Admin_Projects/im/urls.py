from django.conf.urls import url

from im import views

urlpatterns = [
    
    url(r'^$', views.index, name='im_index'),
#     url(r'^$', views.index),

    url(r'^index/$', views.index, name='im_index'),
    
    url(r'^im_actions/$', views.im_actions, name='im_actions'),

    url(r'^time/$', views.today_is, name='todays_time'),
    
]
