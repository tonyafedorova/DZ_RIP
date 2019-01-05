from dzrip.views import PictureRemoveView, PictureView
from django.urls import path

urlpatterns = [
    path('remove/', PictureRemoveView.as_view(), name='picture_remove'),
    path('pictures/', PictureView.as_view(), name='picture_url')
]