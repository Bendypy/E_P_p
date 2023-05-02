"""E_P_p URL Configuration

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
from django.urls import path,  include
import debug_toolbar
from django.utils.translation import gettext as _

admin.site.site_header = _('project management')
admin.site.site_title = _('project management')
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('projects.urls')),
    path('accounts/', include('accounts.urls')),
    path('مح.منصةفنون.مد/', admin.site.urls),
]
