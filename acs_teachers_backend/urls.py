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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.templatetags.static import static as static_file
from rest_framework_swagger.views import get_swagger_view


# https://django-rest-swagger.readthedocs.io/en/latest/
schema_view = get_swagger_view(title='ACS API')


urlpatterns = [
    # grappelli URLS (custom admin panel)
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
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
