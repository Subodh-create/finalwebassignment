from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=False)
    date  = models.DateField(null=False,blank=False,verbose_name="Appointment Date")
    phone = models.CharField(max_length=14,null=False,blank=False)
    desp = models.TextField(null=False,blank=False,verbose_name="Message")
    email = models.EmailField(max_length=90,null=False,blank=False)
    choices = (
        ("pending","Pending"),
        ("accepted","Accepted"),
        ("rejected","Rejected")
    )
    status = models.CharField(max_length=10,choices=choices,default="pending",null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    appto = models.ForeignKey(User,verbose_name="Appointed to",on_delete=models.SET_NULL,null=True,blank=True,related_name="appto")
    photo = models.ImageField(verbose_name="Picture your message",null=True,blank=True)
    def __str__(self):
        return f"{self.user}'s appointment for {self.date}"