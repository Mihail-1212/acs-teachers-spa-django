"""acs_teachers_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.templatetags.static import static as static_file

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Swagger view instance
schema_view = get_schema_view(
   openapi.Info(
      title="Journal and Lessons api",
      default_version='v1',
      description="Api for auto control system site",
      contact=openapi.Contact(email="m.a.mokruschin@yandex.ru"),    # TODO: get from .env
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # Admin routes
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

    # path('swagger/', schema_view),
    # Swagger routes
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Auth routes
    path('authorization/', include('authorization.urls')),

    # API routes
    path('api-journal/', include('journal.urls')),
]


# https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-static-files-during-development
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Add favicon to url path
favicon_view = RedirectView.as_view(url=static_file('icons/favicon.ico'), permanent=True)
urlpatterns.append(path('favicon.ico/', favicon_view))
