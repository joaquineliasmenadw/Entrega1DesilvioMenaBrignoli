from django.urls import path
from Hammer.views import hammer, contacto, create_empleado_view,create_empleador_view,create_servicio_view,search_servicio_view

urlpatterns = [
    path('',hammer, name='hammer'),
    path('contacto/',contacto, name='contacto'),
    path('create-servicio/',create_servicio_view, name='create-servicio'),
    path('create-empleado/',create_empleado_view, name='create-empleado'),
    path('create-empleador/',create_empleador_view, name='create-empleador'),
    path('search-servicio/',search_servicio_view, name='search-servicio'),
]