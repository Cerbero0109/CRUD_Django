from django.urls import path 
from .import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('libros',views.libros, name='libros'),
    path('libros/crear',views.crear, name='crear'),
    path('libros/editar/<int:id>',views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar,name='eliminar'),
    path('acerca',views.acerca, name='acerca'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


