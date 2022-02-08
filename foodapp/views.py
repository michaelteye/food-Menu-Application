from dataclasses import field, fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView,CreateView,TemplateView
from .models import Menu
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MainHomePage(TemplateView):
    template_name = 'foodapp/home.html'


class HomePageView(LoginRequiredMixin,ListView):
    model = Menu
    context_object_name = 'object_list'
    template_name = 'foodapp/index.html'
    login_url = 'login'

class DetailPageView(LoginRequiredMixin,DetailView):
    model = Menu
    template_name = 'foodapp/detail.html'
    login_url = 'login'

class UpdateViewPage(UpdateView):
    model = Menu
    template_name = 'foodapp/update.html'
    fields = ('name', 'description', 'image')
    # success_url = reverse_lazy('detail')

class CreateViewPage(CreateView):
    model = Menu
    template_name = 'foodapp/create.html'
    fields = '__all__'
    # success_url = reverse_lazy('index')

class DeleteViewPage(DeleteView):
    model = Menu
    template_name = 'foodapp/delete.html'
    success_url = reverse_lazy('index')
