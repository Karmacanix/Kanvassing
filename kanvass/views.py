from typing import Any
from django.shortcuts import render
from django.forms import ModelForm, BaseModelFormSet, modelform_factory, Textarea
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from .models import Kanvass


# Create your views here.
class KanvassListView(ListView):
    model = Kanvass
    context_object_name = "kanvass_list"
    template_name = "kanvass_list.html"
    

class KanvassCreateView(CreateView):
    model = Kanvass
    fields = '__all__'
    template_name = "kanvasss/kanvass_form.html"


class KanvassUpdateView(UpdateView):
    context_object_name = "current_kanvass"
    model = Kanvass
    success_url = '/kanvass/list/'
    fields = '__all__'
    template_name = "kanvasss/kanvass_form.html"
    

class KanvassDetailView(DetailView):
    context_object_name = "current_kanvass"
    model = Kanvass
    fields = '__all__'
    template_name = "kanvasss/kanvass_detail.html"