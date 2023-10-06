# courses/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registro_form, name="registro_form"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('foro/', views.course_foro, name='foro'),
    # path('register/', views.signup, name='signup'),
    path('contact/', views.course_contact, name='contact'),
    path('courseAvailable/', views.course_available, name='courseAvailable'),
    path('', views.index, name='index'),
]
