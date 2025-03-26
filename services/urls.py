from django.urls import path
from .views import *

urlpatterns = [
    path('services', ServicesListView.as_view()),
    path('services', ServicesCreateView.as_view()),
    path('services/<int:pk>', ServiceUpdateView.as_view()),
    path('services/destroy/<int:pk>', ServiceDestroyView.as_view()),
    path('services/retrieve/<int:pk>', ServiceRetrieveView.as_view()),
    path('docentes', DocenteListView.as_view()),
    path('docentes', DocenteCreateView.as_view()),
    path('docentes/<int:pk>', DocenteUpdateView.as_view()),
    path('docentes/destroy/<int:pk>', DocenteDestroyView.as_view()),
    path('docentes/retrieve/<int:pk>', DocenteRetrieveView.as_view()),
    path('grados', GradoListView.as_view()),
    path('grados', GradoCreateView.as_view()),
    path('grados/<int:pk>', GradoUpdateView.as_view()),
    path('grados/destroy/<int:pk>', GradoDestroyView.as_view()),
    path('alumnos', AlumnoListView.as_view()),
    path('alumnos', AlumnoCreateView.as_view()),
    path('alumnos/<int:pk>', AlumnoUpdateView.as_view()),
    path('alumnos/destroy/<int:pk>', AlumnoDestroyView.as_view()),
    path('alumnos/retrieve/<int:pk>', AlumnoRetrieveView.as_view()),
    path('alumnos/grado/<int:id_grado>', AlumnoPorGradoListView.as_view()),

]