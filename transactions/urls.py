from django.urls import path
from .views import *

urlpatterns = [
    path('matricula',MatriculaListView.as_view()),
    path('pagos/create/<int:id_matricula>',PagosCreateView.as_view())
]