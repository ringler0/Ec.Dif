from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import json
from gestion.models import datos_uma


def getAll(request):
    asd=datos_uma.objects.all()
    data={"foo": "bar"}
    return HttpResponse(asd.query, content_type="application/json")

def getValue(request):
    latitud = request.GET.get('lat', '')
    longitud = request.GET.get('long', '')
    asd=datos_uma.objects.filter(lat=latitud,lon=longitud)
    return HttpResponse(asd)