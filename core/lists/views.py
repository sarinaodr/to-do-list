from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from .models import ToDoList
from .forms import ListForm

# Create your views here.
class DoList(LoginRequiredMixin , ListView):
    model = ToDoList
    paginate_by = 30
    

    context_object_name = 'posts'
    
class ListDetailView(LoginRequiredMixin , DetailView):
    model = ToDoList
    
class ListCreateView(LoginRequiredMixin , CreateView):
    model = ToDoList
    form_class = ListForm
    success_url = '/blog/list/'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
    
class ListEditView(LoginRequiredMixin , UpdateView):
    model = ToDoList
    form_class = ListForm
    success_url = '/blog/list/'
    
class ListDeleteView(LoginRequiredMixin , DeleteView):
    model = ToDoList
    success_url = '/blog/list/'