from django.conf.urls import include, url
from gituser.views import ShowResult, SearchQuery
from rest_framework import routers
router = routers.SimpleRouter()


urlpatterns = [
    url(r'^ShowResult', ShowResult.as_view()),
    url(r'^SearchQuery', SearchQuery.as_view()),
    url(r'^', include(router.urls)),
]