"""edashboard URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'edashboard'
urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.construction_view, name='index'),
    path('building/', views.building_view, name='building'),
    path('compare/', views.compare_view, name='compare'),
    path('export/', ExportView.as_view(), name='export'),
    path('export/data/', ExportView.as_view(), name='exportdata'),
    path('export/data/', views.get_data, name='exportdata'),
    path('help/', views.help_view, name='help'),
    path('login/', views.login_view, name='login'),
    path('adminsite/', views.admin_view, name='adminsite'),
    path('construction/', views.construction_view, name='construction'),
    path('connection/',views.formView, name = 'loginform'),
    path('loginn/', views.login, name='loginn'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
