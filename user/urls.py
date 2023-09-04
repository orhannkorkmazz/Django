from django.urls import path

from . import views
app_name="user"
urlpatterns = [
    path('user/register', views.register,name="register"),
    path('user/login', views.loginUser,name="login"),
    path('user/logout', views.logoutUser,name="logout"),
]