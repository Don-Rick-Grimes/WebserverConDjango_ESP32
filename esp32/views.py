from xml.etree.ElementTree import tostring
from django.http import JsonResponse
from django.shortcuts import render
import requests, json
# Create your views here.
ip_esp32 = "http://192.168.0.97"
def esp32(request):
    estado=''
    if request.method=="POST":
        bodyData=json.loads(request.body)
        accion = bodyData['Accion']
        if accion == "Encender":
            r = requests.get(f'{ip_esp32}/H')
            return JsonResponse({"Estado":r.text})
        elif accion == "Apagar":
            r = requests.get(f'{ip_esp32}/L')
            return JsonResponse({"Estado":r.text})

    return render(request, "esp32/esp32wifi.html",{'Estado':estado})

       

