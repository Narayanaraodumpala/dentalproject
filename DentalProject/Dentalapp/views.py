from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import DoctorsModel


class Homepage(ListView):
    template_name = 'homepage.html'
    model = DoctorsModel
    queryset = DoctorsModel.objects.all()
    paginate_by = 3
