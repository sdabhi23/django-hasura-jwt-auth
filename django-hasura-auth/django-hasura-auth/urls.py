"""django-hasura-auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import HasuraTokenObtainPairView, CreateUserView, UserDetails

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Django JWT Auth API',
        default_version='v1',
        description='A simple containerized JWT based auth server written using Django, Djoser and Django Rest Framework',
        contact=openapi.Contact(email='shrey.dabhi23@gmail.com'),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    url(r'^$', schema_view.with_ui('swagger',
                                   cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('user/', CreateUserView.as_view(), name='create_user'),
    path('user/me/', UserDetails.as_view(), name='get_user'),
    path('token/', HasuraTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json')
]
