# courses/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registro, name="registro"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('foro/', views.course_foro, name='foro'),    
    path('contact/', views.contact, name='contact'),
    path('registro/', views.registro, name='registro'),
    path('abm/', views.estudianteListView.as_view(), name='abm_user'),
    path('abm/baja/<int:pk>', views.estudianteDelete.as_view(), name='baja_estudiante'),
    path('abm/modificar/<int:pk>', views.estudianteUpdate.as_view(), name='modificar_estudiante'),
    path('courseAvailable/', views.course_available, name='courseAvailable'),
    path('', views.index, name='index'),
]
