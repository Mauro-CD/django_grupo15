# courses/urls.py
from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('admin/', views.admin, name='admin_total'),
    path('register/', views.registro, name="registro"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    
    path('courses/', views.course_list, name='course_list'),
    path('courses/edit', views.course_edit.as_view(), name='course_edit'),
    path('courses/edit/nuevo', views.courseCreateView.as_view(), name='course_nuevo'),
    path('courses/edit/baja/<int:pk>', views.cursoDelete.as_view(), name='baja_curso'),
    path('courses/edit/<int:pk>', views.cursoUpdate.as_view(), name='modificar_curso'),

    path('courses/inscripciones', views.inscripcionesListView.as_view(), name='curso_estudiante'),
    path('courses/inscripciones/nuevo', views.inscripcionesCreateView.as_view(), name='curso_estudiante_alta'),
    # path('courses/inscripciones/nuevo/<int:estudiante_id>/<int:curso_id>/', views.alta_inscripcion, name='alta_inscripcion'),
    path('courses/inscripciones/baja/<int:pk>', views.inscripcionesDelete.as_view(), name='curso_estudiante_delete'),
    path('courses/inscripciones/baja/<int:estudiante_id>/<int:curso_id>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),


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

    #path('courseAvailable/', views.course_available, name='courseAvailable'),original
    path('courseAvailable/', views.cursos_from_db, name='courseAvailable'),
    path('pagocurso/', views.pago, name='pago'),
    path('', views.index, name='index'),
]
