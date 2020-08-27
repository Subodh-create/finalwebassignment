from django.shortcuts import render,redirect
from django.views import View
from dashboard import forms,models

# Create your views here.
class Home(View):
    def get(self,request):
        aform = forms.AppointmentForm()
        return render(request,"home/index.html",{"aform":aform})

    def post(self,request):
        if request.user.is_authenticated:
            aform = forms.AppointmentForm(request.POST,request.FILES)
            if aform.is_valid():
                appoint = aform.save(commit=False)
                appoint.user = request.user
                appoint.status = "pending"
                appoint.save()
                return redirect('dashboard')
            else:
                return render(request,"home/index.html",{"aform":aform})
        else:
            return redirect("login")