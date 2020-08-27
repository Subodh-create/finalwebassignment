from django.urls import path
from . import views

urlpatterns = [
    path("",views.AppointListView.as_view(),name="dashboard"),
    path("<int:id>/edit/",views.AppointEditView.as_view(),name="editapp"),
    path("<int:id>/delete/",views.AppointDeleteView.as_view(),name="deleteapp"),
    path("status/",views.SubForm.as_view(),name="submit"),
]