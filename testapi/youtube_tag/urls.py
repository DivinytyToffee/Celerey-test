from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('words', csrf_exempt(views.SetTags.as_view()), name='words'),
    path('words/<int:tag_id>', csrf_exempt(views.SetTags.as_view()), name='words'),
    path('words/<int:tag_id>/video', csrf_exempt(views.GetTags.as_view()), name='video'),
]
