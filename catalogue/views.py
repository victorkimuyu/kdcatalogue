from django.views import generic
from .models import Kayak
from .forms import KayakForm


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
        features = self.object.key_features.split('\n')
        context['features'] = [x for x in features if x != '']
        context['kayaks'] = Kayak.kayaks.all()

        base_url = "https://res.cloudinary.com/kimuyu/image/upload/v1661335568/kd/kayaks/" + self.object.brand.replace(
            " ", "%20")
        photo_url = base_url + "/" + self.object.model_name.replace(" ", "_").replace("”", "").replace("'", "").replace(
            "'", "") + ".jpg"

        context["photo_url"] = photo_url

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
