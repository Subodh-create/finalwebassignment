from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("",views.Home.as_view(),name="home"),
    path("aboutus/",TemplateView.as_view(template_name="home/about-us.html"),name="about-us"),
    path("contact/",TemplateView.as_view(template_name="home/contact.html"),name="contact"),
    path("services/",TemplateView.as_view(template_name="home/services.html"),name="services"),

]