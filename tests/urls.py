from django.conf.urls.defaults import url, patterns, include
from .app.views import TestView

urlpatterns = patterns(
    '',
    url('^', include('mob.urls', namespace = 'mob')),
    url('^$', TestView.as_view()),
)
