"""chunked_upload_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('admin/', admin.site.urls),
    path('uploads/', include(('uploads.urls', 'uploads')), name='uploads'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
