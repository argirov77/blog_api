"""blog_project URL Configuration

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
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as yasg_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Настройка для drf-yasg (Swagger и Redoc)
swagger_schema_view = yasg_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="A Web API for creating and editing blog posts.",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# Настройка для стандартной схемы Django REST Framework
openapi_schema_view = get_schema_view(
    title="Blog API Schema",
    description="OpenAPI schema for the Blog API",
    version="1.0.0",
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # Swagger и Redoc
    path('docs/', swagger_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', swagger_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Стандартная схема
    path('schema/', openapi_schema_view, name='openapi-schema'),
]
