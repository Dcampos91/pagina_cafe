from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cafe', CafeViewSet)

urlpatterns = [
    path('', index,name="index"),
    path('modificar/<id>/', modificar,name="modificar"),
    path('eliminar_cafe/<id>/', eliminar_cafe,name="eliminar_cafe"),
    path('pagina2/', pagina2,name="pagina2"),
    path('pagina3/', pagina3,name="pagina3"),
    path('pagina4/', pagina4,name="pagina4"),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('api/', include(router.urls)),
    path('guardar-token/', guardar_token, name='guardar_token'),
]
