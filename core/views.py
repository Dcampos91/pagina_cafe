from django.shortcuts import render, redirect
from .models import Cafe, Cliente
from .forms import CafeForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

#rest_framework
from rest_framework import viewsets
from .serializers import CafeSerializer

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseBadRequest

from django.core import serializers
import json

from fcm_django.models import FCMDevice



# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token, active=True)

    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}))

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}))


def index(request):
    return render(request,'core/index.html')

def modificar(request, id):
    cafe = Cafe.objects.get(id=id)
    data ={
        'form':CafeForm(instance=cafe)
    }
    if request.method == 'POST':
        formulario = CafeForm(data=request.POST, instance=cafe)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
    return render(request,'core/modificar.html',data)

def eliminar_cafe(request, id):
    cafe = Cafe.objects.get(id=id)
    cafe.delete()
    return redirect(to="pagina3")

def pagina2(request):
    return render(request,'core/Pagina2.html')
#guardar cafe
@permission_required('core.add_cafe')
def pagina3(request):
    cafe = Cafe.objects.all()
    data = {
        'cafe':cafe,
        'form':CafeForm()
    }
    if request.method == 'POST':
        formulario = CafeForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            dispositivo = FCMDevice.objects.filter(active=True)
            dispositivo.send_message(
                title="Cafe agregado !!!",
                body="Se ha agregado un cafe " + formulario.cleaned_data['nombre_cafe'],
                icon="/static/core/IMG/logo.png"
            )
            data ['mensaje'] = 'Guardado Correctamente'


    return render(request,'core/Pagina3.html',data)


def pagina4(request):
    return render(request,'core/Pagina4.html')

#resivir datos o hacer consulta
class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html', data)
