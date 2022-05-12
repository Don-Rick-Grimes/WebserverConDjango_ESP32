from xml.etree.ElementTree import tostring
from django.http import JsonResponse
from django.shortcuts import render
import requests, json
# Create your views here.
ip_esp32 = "http://192.168.0.97"
def esp32(request):
    def sendToEsp32(url):
        try:
            r = f'{requests.get(url).text}'
        except(requests.ConnectionError):
            r = '{"Estado":"Error de conexion"}'    

        return r

    if request.method=="POST":
        bodyData=json.loads(request.body)
        accion = bodyData['Accion']
        if accion == "Encender":
            r = sendToEsp32(f'{ip_esp32}/H')
            rJson = json.loads(r)
            return JsonResponse({'Estado':rJson['Estado']})
        elif accion == "Apagar":
            r = sendToEsp32(f'{ip_esp32}/L')
            rJson = json.loads(r)
            return JsonResponse({'Estado':rJson['Estado']})
        elif accion == "Conectar":
            r = sendToEsp32(ip_esp32)
            rJson = json.loads(r)
            return JsonResponse({'Estado':rJson['Estado']})

    return render(request, "esp32Websockets/esp32wifi.html")

       

