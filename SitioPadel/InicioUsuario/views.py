from django.shortcuts import render

def view_inicio_usuario(request):
    return render(request,'InicioUsuario/inicio_usuario.html',{})
# Create your views here.
