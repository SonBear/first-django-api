from django.urls import path

from . import views

urlpatterns = [
    path('alumnos', views.index_students, name='index_students'),
    path('alumnos-create', views.save_students, name='save_students'),
]