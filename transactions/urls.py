from django.urls import path
from .views import *

urlpatterns = [
    path('matricula',MatriculaListView.as_view())
]