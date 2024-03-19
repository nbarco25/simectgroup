
from django.urls import path
from .views import index
from .views import enviar_correo
from .views import nosotros_view

urlpatterns = [
    path('', index, name='base'),
    path('enviar-correo/', enviar_correo, name='enviar_correo'),
    path('nosotros/', nosotros_view, name='nosotros'),

]
