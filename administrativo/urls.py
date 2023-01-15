from django.urls import path
from .views import *
from django.urls import path, include

app_name='administrativo'




urlpatterns = [
    path("emprendimientos/<int:id_emprendimiento>/",VerEmprendimiento.as_view(),name ='detalleEmprendimientos'),
    path('emprendimientos/listado/<int:id_servicio>',ListarEmprendimientos.as_view(),name='listadoEmprendimientos' ),
    path('emprendimientos/reserva/<int:id_producto>',GenerarReserva.as_view(),name='reserva' ),
    path('index', Index.as_view(), name="index"),
]

