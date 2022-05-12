from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, "proyecto_web1App/home.html")


