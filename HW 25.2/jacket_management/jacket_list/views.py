from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Jacket
from .forms import JacketForm

class JacketListView(ListView):
    model = Jacket
    template_name = "jacket_list.html"
    context_object_name = "jackets"

class JacketCreateView(CreateView):
    model = Jacket
    form_class = JacketForm
    template_name = "jacket_form.html"
    success_url = reverse_lazy('jacket-list')

class JacketDetailView(DetailView):
    model = Jacket
    template_name = "jacket_detail.html"
    context_object_name = "jacket"

class JacketUpdateView(UpdateView):
    model = Jacket
    form_class = JacketForm
    template_name = "jacket_form.html"
    success_url = reverse_lazy('jacket-list')

class JacketDeleteView(DeleteView):
    model = Jacket
    template_name = "jacket_confirm_delete.html"
    success_url = reverse_lazy('jacket-list')
