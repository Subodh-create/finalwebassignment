'''
All of the forms handling are done in home app 
'''
from django.http import HttpResponseForbidden
from django.views import View,generic
from django.shortcuts import render,redirect
from . import models,forms
from django.contrib.auth.mixins import LoginRequiredMixin

#lisitng appointments
# dashboard home
class AppointListView(LoginRequiredMixin,generic.ListView):
    model = models.Appointment
    #achronnym for appountment 
    context_object_name = "apps"
    template_name = "dashboard/listview.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        qs = super().get_context_data()
        
        if self.request.user.profile.utype == "DOC":
            qs['user']  =  models.Appointment.objects.filter(status="pending").order_by("-date")
            print("DOCTOR USER")
            qs['pc']   =  models.Appointment.objects.filter(status="pending").count()
            qs['pr']   =  models.Appointment.objects.filter(status="rejected").count()
            qs['pa']   =  models.Appointment.objects.filter(status="accepted").count()

        else:
            qs['user'] =  models.Appointment.objects.filter(user= self.request.user).order_by("-date")
            print("NORMAL USER")
            qs['pc']   =  models.Appointment.objects.filter(user= self.request.user,status="pending").count()
            qs['pr']   =  models.Appointment.objects.filter(user= self.request.user,status="rejected").count()
            qs['pa']   =  models.Appointment.objects.filter(user= self.request.user,status="accepted").count()
        return qs

    def post(self,request):
        currApp = models.Appointment.objects.get(id= request.POST.get("appid"))
        currApp.status = request.POST.get("status")
        currApp.message = request.POST.get("message")
        currApp.appto = request.user
        currApp.save()
        return redirect("dashboard")


class AppointEditView(View):
    def dispatch(self, request,id, *args, **kwargs):
        currApp = models.Appointment.objects.get(id= id) or None
        if request.user == currApp.user:
            return super().dispatch(request,id, *args, **kwargs)
        else:
            return  HttpResponseForbidden("Not allowed")

    def get(self,request,id):
        currApp = models.Appointment.objects.get(id= id) or None
        aform = forms.AppointmentForm(instance=currApp)
        return render(request,"dashboard/editform.html",{"aform":aform})

    def post(self,request,id):
        currApp = models.Appointment.objects.get(id= id) or None 
        aform = forms.AppointmentForm(request.POST,request.FILES,instance=currApp)
        if aform.is_valid():
            aform.save(commit=True)
            return redirect("dashboard")
        else:
            return render(request,"dashboard/editform.html",{"aform":aform})


class AppointDeleteView(View):
    def dispatch(self, request,id, *args, **kwargs):
        currApp = models.Appointment.objects.get(id= id) or None
        if request.user == currApp.user:
            return super().dispatch(request,id, *args, **kwargs)
        else:
            return  HttpResponseForbidden("Not allowed")

    def get(self,request,id):
        currApp = models.Appointment.objects.get(id= id) or None
        return render(request,"dashboard/delete.html",{"obj":currApp})

    def post(self,request,id):
        currApp = models.Appointment.objects.get(id= id) or None 
        currApp.delete()
        return redirect("dashboard")
        
class SubForm(View):
    def post(self,request, *args, **kwargs):
        currApp = models.Appointment.objects.get(id= request.POST.get('id')or None) or None 
        currApp.status =  request.POST.get("status")
        currApp.save()
        return redirect("dashboard")

