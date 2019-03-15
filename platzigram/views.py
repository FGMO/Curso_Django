from django.http import HttpResponse, JsonResponse
from datetime import datetime
import pdb
import json


def numeros(request):
    # pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers.sort()
    # respuesta = JsonResponse(
    #     sorted([int(i) for i in request.GET['numbers'].split(',')]), safe=False
    # )
    # respuesta = JsonResponse(numbers, safe=False)

    datos = {
        'mensaje': 'ok',
        'numeros': numbers
    }

    return HttpResponse(json.dumps(datos, indent=7), content_type='application/json')


def edad(request, nombre, edad):
    if edad < 18:
        respuesta = '{} es menor de edad.'.format(nombre)
    else:
        respuesta = '{} es mayor de edad'.format(nombre)
    return HttpResponse(respuesta)