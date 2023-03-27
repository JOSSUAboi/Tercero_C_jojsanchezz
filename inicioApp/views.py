from django.http import HttpRequest
from django.shortcuts import render
from inicioApp.forms import formulariouser
from inicioApp.models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request,  'registration/login.html')


def inicioDef(request):
      return render(request,'inicio.html',{})

def mantenDef(request):
      return render(request,'mantemiento.html',{})

#def  registro(request):
   #   return render(request, 'registro.html')


class formularioafiview(HttpRequest):
      def index(request):
            usuario=formulariouser()
            return render(request, "estudiantes.html", {"form":usuario})
      def procesar_formulario(request):
            usuario=formulariouser(request.POST)
            if usuario.is_valid():
                  usuario.save()
                  usuario=formulariouser()
            return render(request, "estudiantes.html", {"form":usuario, "mensaje": 'ok'})

      def listar_usuario(request):
            usuario = Usuario.objects.all()
            return render(request,"lista_registros.html",{"usuario" : usuario})

      def edit(request, id_usuario):
            usuario= Usuario.objects.filter(id=id_usuario).first()
            form = formulariouser(instance=usuario)
            return render(request,"editar_estudiante.html",{"form":form, 'usuario': usuario})

      def actualizar_usuario(request, id_usuario,):
            usuario=Usuario.objects.get(pk=id_usuario)
            form= formulariouser(request.POST, instance=usuario)
            if form.is_valid():
                  form.save()
            usuario=Usuario.objects.all()
            return render(request,"lista_registros.html",{"usuario":usuario})


      def delete(request, id_usuario):
            usuario = Usuario.objects.get(pk=id_usuario)
            usuario.delete()
            usuario= Usuario.objects.all()
            return render(request,"lista_registros.html",{"usuario": usuario, "mensaje": 'Ok'})
