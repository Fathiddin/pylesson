from django.urls import path

from main import views
from . import *
app_name="main"

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('category/<slug:slug>', views.category_post, name='category_post')
]