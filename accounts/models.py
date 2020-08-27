from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    choices = (
        #normal user
        ("NU","NU"),
        #doctor
        ("DOC","DOC"),
    )
    utype = models.CharField(max_length=3,choices=choices,default="NU",blank=False,null=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return f"{self.user.username} is {self.utype}"