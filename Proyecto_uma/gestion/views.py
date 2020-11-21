from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from json import dumps
from gestion.models import datos_uma

def getAll(request):
    asd=datos_uma.objects.all()
    #data = {"asf":"asf"}
    #return HttpResponse(dumps(data), content_type='application/json')
    return HttpResponse(asd)

def getValue(request):
    latitud = request.GET.get('lat', '')
    longitud = request.GET.get('long', '')
    asd=datos_uma.objects.filter(lat=latitud,lon=longitud)
    return HttpResponse(asd)