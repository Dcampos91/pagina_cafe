from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="index"),
    path('modificar/<id>/', modificar,name="modificar"),
    path('eliminar_cafe/<id>/', eliminar_cafe,name="eliminar_cafe"),
    path('pagina2/', pagina2,name="pagina2"),
    path('pagina3/', pagina3,name="pagina3"),
    path('pagina4/', pagina4,name="pagina4"),
]
