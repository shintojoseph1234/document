"""
URL Configuration for api app
"""
# Django imports
from django.urls import include, path
# rest_framework imports
from rest_framework import routers
# local imports
from api import views

# select the router
router = routers.DefaultRouter()
# register the ContentViewSet
router.register('content', views.ContentViewSet)
router.register('tag', views.TagViewSet)

app_name = 'api'

urlpatterns = [
    # include router urls
    path('', include(router.urls)),
]
