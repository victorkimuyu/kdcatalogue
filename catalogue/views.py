from django.shortcuts import render
from django.views import generic
from .models import Kayak
from.forms import KayakForm


class KayakList(generic.ListView):
    model = Kayak
    context_object_name = 'kayaks'
    template_name = 'catalogue/kayak-list.html'


class KayakDetail(generic.DetailView):
    model = Kayak
    context_object_name = 'kayak'
    template_name = 'catalogue/kayak-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kayaks'] = Kayak.kayaks.all()
        return context


class KayakCreate(generic.CreateView):
    model = Kayak
    form_class = KayakForm
    template_name = 'catalogue/kayak-create.html'
