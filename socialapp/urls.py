
from django.conf.urls import patterns, url

from views import SocialView,LogoutView


urlpatterns = patterns(
    '',
    url(r'^$', SocialView.as_view(), name='social'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
)


