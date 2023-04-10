from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontPage, name='frontPage' ),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name="logout_user"),
    path('login/', views.user_login, name="login"),
]