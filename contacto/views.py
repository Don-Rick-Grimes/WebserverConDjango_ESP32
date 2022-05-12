from django.conf import settings
from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method=="POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            try:
                send_mail("Mensaje desde App Django",f"Nombre usurario: {nombre}\nEmail usuario: {email}\nEscribe los siguiente: \n\n{contenido}","",[settings.EMAIL_HOST_USER],fail_silently=False)
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?envioFallo")

    return render(request, "contacto/contacto.html", {"miFormulario":formulario_contacto})