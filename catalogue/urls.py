from django.urls import path
from .views import KayakCreate, KayakUpdate, KayakDetail, KayakList
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('kayaks/new/', KayakCreate.as_view(), name='kayak-create'),
                  path('kayaks/<slug:slug>/update/', KayakUpdate.as_view(), name='kayak-update'),
                  path('kayaks/<slug:slug>/', KayakDetail.as_view(), name='kayak-detail'),
                  path('kayaks/', KayakList.as_view(), name='kayak-list'),
                  path('', KayakList.as_view(), name='kayak-list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
