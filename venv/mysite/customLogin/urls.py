from django.urls import path
from . import views
from django.conf.urls import url, include

app_name = 'customLogin'
urlpatterns = [
    path(r'user_create/', views.UserCreate.as_view(), name='user_create'),
    path(r'user_login', views.CustomLoginView.as_view(), name='login'),
]
