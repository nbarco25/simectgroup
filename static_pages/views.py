from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'base.html')

def nosotros_view(request):
    return render(request, 'sections/nosotros.html')

def hablemos_view(request):
    return render(request, 'sections/contacto.html')



def enviar_correo(request):
    if request.method == 'POST':
        nombre = request.POST.get('firstName')
        apellido = request.POST.get('lastName')
        email = request.POST.get('email')
        telefono = request.POST.get('phone')
        mensaje = request.POST.get('message')
        
        # Enviar correo electrónico
        send_mail(
            'Nuevo mensaje de contacto',
            f'Nombre: {nombre} {apellido}\nEmail: {email}\nMensaje: {mensaje}' + f'\nTelefono: {telefono}',
            email,
            ['anbarco@unicauca.edu.co'],  # Dirección de correo electrónico de destino
            fail_silently=False,
        )
        return HttpResponse('Correo enviado exitosamente')
    else:
        return HttpResponse('No se ha enviado el formulario correctamente')
