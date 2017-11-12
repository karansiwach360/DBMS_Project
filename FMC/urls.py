"""fmc URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url(r'^clubs/$', views.clubs,name='clubs'),
    url(r'^home/$',views.home,name='home'),
    url(r'^people/$',views.people,name='people'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/logged_out'}, name='logout'),
    url(r'^logged_out/$',views.logged_out, name='logged_out'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^postholders/$',views.postholders,name='postholders'),
    url(r'^members/$',views.members,name='members'),
    url(r'^alumni/$',views.alumni,name='alumni'),
    url(r'^allusers/$',views.allusers,name='allusers'),
    url(r'^events/$',views.events,name='events'),
    url(r'^pastevents/$',views.pastevents,name='pastevents'),
    url(r'^presentevents/$',views.presentevents,name='presentevents'),
    url(r'^support/$',views.support,name='support'),
    url(r'^resources/$',views.resources,name='resources'),
    url(r'^merchandise/$',views.merchandise,name='merchandise'),
    url(r'^funds/$',views.funds,name='funds'),
]
