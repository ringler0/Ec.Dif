from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import json
from gestion.models import datos_uma
from django.http import JsonResponse


def getAll(request):
    asd=datos_uma.objects.all()
    data={"foo": "bar"}
    return HttpResponse(asd)
    #return HttpResponse(asd.query, content_type="application/json")

def getValue(request):
    latitud = request.GET.get('lat', '')
    longitud = request.GET.get('long', '')
    query=datos_uma.objects.filter(lat=latitud,lon=longitud)
    lr=[entry for entry in query]
    t=str(lr)
    lim=t[2:-2]
    json={
        'result':lim
    }
    #return HttpResponse(query)
    return JsonResponse(json)