from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login.as_view(),name="login"),
    path('signin/',views.Signin.as_view(),name="signin"),
    path('logout/',views.logout_user,name="logout"),
]