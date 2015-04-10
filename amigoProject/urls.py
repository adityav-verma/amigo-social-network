from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

#a new class overriding the bahaviour of default regisration
class MyRegistratioView(RegistrationView):
	#overriding the default view and telling it to use the form which requires unique email id
	form_class = RegistrationFormUniqueEmail
	def get_success_url(self, request, user):
		return '/amigo/addProfile/'



urlpatterns = [
    # Examples:
    # url(r'^$', 'amigoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^amigo/', include('amigo.urls')),
    url(r'^accounts/register/$', MyRegistratioView.as_view(), name = 'registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )