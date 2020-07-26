"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token, verify_jwt_token
    )
from rest_framework.documentation import include_docs_urls
admin.site.site_header = "Admin  @WOMCS"
admin.site.site_title = "WOMCS Admin Portal"
admin.site.index_title = "Welcome to WOMCS Admin Portal"



urlpatterns = [
	path('admin/', admin.site.urls),
    path('api/v1/auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/token/obtain', obtain_jwt_token),
    path('api/v1/token/refresh', refresh_jwt_token),
    path('api/v1/token/verify', verify_jwt_token),
    #path('api/v1/', include('project.apiurls')),
    path(r'docs/', include_docs_urls(title='Polls API')),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
