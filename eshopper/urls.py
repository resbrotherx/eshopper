"""eshopper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.conf import include
from api import urls as api_urls
from items import urls as items_urls
from django.conf.urls.static import static
from django.conf import settings
from user import views as as_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('', include(items_urls)),
    path('prints/', include('prints.urls')),
    path('graphics/', include('Graphics.urls'), name='Graphics'),
    path('register/', as_view.register, name='register'),
    path('profile/', as_view.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('tinymce/', include('tinymce.urls')),


     path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)