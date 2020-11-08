from django.contrib import admin
from .models import DoctorsModel,Next3Dentist,AnotherNext3Dentist
# Register your models here.
admin.site.register(DoctorsModel)
admin.site.register(Next3Dentist)
admin.site.register(AnotherNext3Dentist)