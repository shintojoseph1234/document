"""
URL Configuration for document project
"""
# django imports
from django.contrib import admin
from django.urls import include, path
# REST imports
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views
# Swagger imports
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title             = "Document API",
      default_version   = 'v1',
      terms_of_service  = "",
      description       = "Document description",
      license           = openapi.License(name="BSD License"),
      contact           = openapi.Contact(email="shintojoseph1234@gmail.com"),
   ),
   public               = True,
   permission_classes   = (permissions.AllowAny,),
)

urlpatterns = [
    # admin urls
    path('admin/', admin.site.urls),
    # include api urls
    path('api/', include('api.urls', namespace="api")),
    # swagger url
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    # swagger API views
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    # API doc urls
    path('docs/', include_docs_urls(title='Document API', public=True)),
    # GET token
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    # GET refresh token
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
]
