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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'edashboard'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home/', views.index, name='home'),
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='edashboard/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='edashboard/index.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('building/', views.building_view, name='building'),
    path('building/<buildnum>/', views.building_view, name='building'),
    path('building/<builddata>/', views.building_view, name='building2'),
    path('compare/', views.compareh_view, name='compare'),
    path('compare/<builddata>/', views.compare_view, name='compare2'),
    path('comparedata/<data>/', views.down_compare, name='down_compare'),
    path('export/', views.exporth_view, name='export'),
    path('export/<builddata>/', views.export_view, name='export2'),
    path('exportdata/<data>/', views.down_export, name='down_export'),
    path('help/', views.help_view, name='help'),
    path('adminsite/', views.admin_view, name='adminsite'),
    path('construction/', views.construction_view, name='construction'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
