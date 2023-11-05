# courses/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registro, name="registro"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/edit', views.course_edit.as_view(), name='course_edit'),
    path('courses/edit/nuevo', views.courseCreateView.as_view(), name='course_nuevo'),
    path('courses/edit/baja/<int:pk>', views.cursoDelete.as_view(), name='baja_curso'),
    path('courses/edit/<int:pk>', views.cursoUpdate.as_view(), name='modificar_curso'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('foro/', views.course_foro, name='foro'),    
    path('contact/', views.contact, name='contact'),
    path('registro/', views.registro, name='registro'),
    path('abm/estudiente', views.estudianteListView.as_view(), name='abm_user'),
    path('abm/estudiente/baja/<int:pk>', views.estudianteDelete.as_view(), name='baja_estudiante'),
    path('abm/estudiente/modificar/<int:pk>', views.estudianteUpdate.as_view(), name='modificar_estudiante'),

    path('abm/docente', views.docenteListView.as_view(), name='abm_docente'),
    path('abm/docente/baja/<int:pk>', views.docenteDelete.as_view(), name='baja_docente'),
    path('abm/docente/modificar/<int:pk>', views.docenteUpdate.as_view(), name='modificar_docente'),
    path('abm/docente/nuevo', views.docenteCreateView.as_view(), name='docente_nuevo'),

    path('courseAvailable/', views.course_available, name='courseAvailable'),
    path('', views.index, name='index'),
]
