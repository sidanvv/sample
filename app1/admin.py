from django.contrib import admin
from .models import *
#first we import all the class from the model by importing model

# Register your models here.


admin.site.register(Details)
#here we are registering model to the admin site
admin.site.register(Teachers)

