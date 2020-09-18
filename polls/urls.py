from django.urls import path
from .views import index, text_to_speech, audio

urlpatterns = [
    path('', index, name="home"),
    path('test/', text_to_speech, name="test"),
    path('download/<str:path>', audio, name="audio"),
]
