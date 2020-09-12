"""TACTRIfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from TACTRIapp.views import index,index1,index2,login,login1,logout,logout1,adminmain,adminmain1,adminadd,adminadd1,adminedit,adminedit1,admindelete,admindelete1







urlpatterns = [
    url(r'^$',index),
    url(r'^index/$',index),
    url(r'^login/$',login),
	url(r'^logout/$',logout),
	url(r'^adminmain/$',adminmain),
	url(r'^adminadd/$',adminadd),
	url(r'^adminedit/$',adminedit),	
    url(r'^adminedit/(\w+)/$',adminedit),	
    url(r'^admindelete/$',admindelete),
    url(r'^admin/', admin.site.urls),
    url(r'^index1/$',index1),
    url(r'^index2/$',index2),
    url(r'^login1/$',login1),
    url(r'^logout1/$',logout1),
    url(r'^adminmain1/$',adminmain1),
    url(r'^adminadd1/$',adminadd1),
    url(r'^adminedit1/$',adminedit1), 
    url(r'^adminedit1/(\w+)/$',adminedit1),   
    url(r'^admindelete1/$',admindelete1),

]
