from django.urls import path
from .views import KayakList, KayakDetail, KayakCreate

urlpatterns = [
    path('', KayakList.as_view(), name='kayak-list'),
    path('kayaks/', KayakList.as_view(), name='kayak-list'),
    path('kayaks/<slug:slug>/', KayakDetail.as_view(), name='kayak-detail'),
    path('kayaks/new/', KayakCreate.as_view(), name='kayak-create'),
]