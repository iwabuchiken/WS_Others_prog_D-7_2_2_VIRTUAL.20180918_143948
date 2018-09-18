"""Admin_Projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from curr import views

urlpatterns = [
    
    url(r'^$', views.index, name='curr_index'),
    
    url(r'^updown_patterns/$', views.updown_patterns, name='updown_patterns'),
    
    url(r'^exec_updown_patterns/$', views.exec_updown_patterns, name='exec_updown_patterns'),
    
    url(r'^correlations/$', views.correlations, name='correlations'),
    
    url(r'^exec_correlations/$', views.exec_correlations, name='exec_correlations'),
    
    url(r'^basics/$', views.basics, name='basics'),
    
    url(r'^gen_peak_data/$', views.gen_peak_data, name='gen_peak_data'),
    
    url(r'^exec_Gen_PeakData/$', views.exec_Gen_PeakData, name='exec_Gen_PeakData'),
    
    url(r'^testers/$', views.testers, name='testers'),
    
    url(r'^tester_BuyUps_SellLows/$', views.tester_BuyUps_SellLows, name='tester_BuyUps_SellLows'),
    
    url(r'^exec_Tester_BuyUps_SellLows/$', views.exec_Tester_BuyUps_SellLows, name='exec_Tester_BuyUps_SellLows'),
    
    # 20180918_134024
    url(r'^tester_BuyUps_SellLows__V2/$', views.tester_BuyUps_SellLows__V2, name='tester_BuyUps_SellLows__V2'),
    
#     url(r'^error/$', views.error, name='error'),
    
    
]
