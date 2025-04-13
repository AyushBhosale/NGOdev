"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

from django.http import HttpResponse
from django.template.loader import get_template

def debug_template(request):
    try:
        # Try to load the template
        template = get_template('account/login.html')
        # If successful, return where it found it
        return HttpResponse(f"Template found at: {template.origin.name}")
    except Exception as e:
        # If failed, return the error
        return HttpResponse(f"Error: {str(e)}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('debug-template/', debug_template),
]
