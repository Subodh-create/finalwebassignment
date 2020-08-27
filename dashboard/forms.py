from django import forms
from . import models
import datetime

class DateInp(forms.DateInput):
    input_type = "date"


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=DateInp)
    class Meta:
        model = models.Appointment
        exclude = ['user','status','appto','answer']
    
    field_order = ['phone','email','date','desp','photo']

    def clean(self):
        data =self.cleaned_data
        if (data['date']<datetime.date.today()):
            raise forms.ValidationError("Plese select upcoming dates")