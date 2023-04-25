from django.urls import path
from .views import PaginaRegistro, ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logeo
from django.contrib.auth.views import LogoutView
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('login/', Logeo.as_view(), name='login'),
               path('crear-tarea', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')]