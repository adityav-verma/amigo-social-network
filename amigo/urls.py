from django.conf.urls import include, url
from amigo import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'amigoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name="index"),
    url(r'^addProfile/$', views.addProfile, name="addProfile"),
    url(r'^home/$', views.home, name="home"),
    url(r'^allUsers/$', views.allUsers, name="allUsers"),
    url(r'^friends/$', views.friends, name="friends"),
    url(r'^statusUpdate/$', views.statusUpdate, name="statusUpdate"),
    url(r'^sendRequest/(?P<uid>[\d]+)/$', views.sendRequest, name="sendRequest"),
    url(r'^acceptRequest/(?P<uid>[\d]+)/$', views.acceptRequest, name="acceptRequest"),
]