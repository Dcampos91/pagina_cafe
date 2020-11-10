from django.shortcuts import render, redirect
from .models import Cafe, Cliente
from .forms import CafeForm

# Create your views here.
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
            data ['mensaje'] = 'Guardado Correctamente'


    return render(request,'core/Pagina3.html',data)


def pagina4(request):
    return render(request,'core/Pagina4.html')
