from django.views import generic
from .models import Kayak
from .forms import KayakForm


class KayakList(generic.ListView):
    model = Kayak
    context_object_name = 'kayaks'
    ordering = ["brand", "is_new"]
    template_name = 'catalogue/kayak-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['riot_kayaks'] = Kayak.kayaks.riot
        context['azul_kayaks'] = Kayak.kayaks.azul
        context['boreal_design'] = Kayak.kayaks.boreal
        context['cobra_kayaks'] = Kayak.kayaks.cobra
        context['riot_sup'] = Kayak.kayaks.riot_sup
        context['kayaks'] = Kayak.kayaks.all()
        return context




class KayakDetail(generic.DetailView):
    model = Kayak
    context_object_name = 'kayak'
    template_name = 'catalogue/kayak-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        features = self.object.key_features.split('\n')
        context['features'] = features
        context['kayaks'] = Kayak.kayaks.all()
        return context


class KayakCreate(generic.CreateView):
    model = Kayak
    form_class = KayakForm
    template_name = 'catalogue/kayak-create.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class KayakUpdate(generic.UpdateView):
    model = Kayak
    form_class = KayakForm
    template_name = 'catalogue/kayak-create.html'

    def get_success_url(self):
        return self.object.get_absolute_url()
