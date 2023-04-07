from django.urls import path
from django.contrib.auth import authenticate, login, logout

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/',views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customize_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record')
]


