from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home.as_view(), name='home'),

]
