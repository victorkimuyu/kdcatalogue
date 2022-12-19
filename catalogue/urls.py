from django.urls import path
from .views import Kayaks, KayakCreate, KayakUpdate, KayakDetail, KayakList
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', Kayaks.as_view(), name='index'),
                  path('staff/kayaks/new/', KayakCreate.as_view(), name='kayak-create'),
                  path('staff/kayaks/<slug:slug>/update/', KayakUpdate.as_view(), name='kayak-update'),
                  path('staff/kayaks/<slug:slug>/', KayakDetail.as_view(), name='kayak-detail'),
                  path('staff/kayaks/', KayakList.as_view(), name='kayak-list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
