from django.shortcuts import render, HttpResponse
import requests

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'codigo' and 'nombre' and 'descripcion' and 'tipoIndicador' and 'prioridad' in request.GET:
        codigo = request.GET['codigo']
        nombre = request.GET['nombre']
        descripcion = request.GET['descripcion']
        tipoIndicador = request.GET['tipoIndicador']
        prioridad = request.GET['prioridad']
        # Verifica si el value no esta vacio
        if codigo:
            # Crea el json para realizar la petición POST al Web Service
            args = {'codigo': codigo, 'nombre' : nombre, 'descripcion' : descripcion, 'tipoIndicador' : tipoIndicador, 'prioridad':prioridad}
            response = requests.post('http://127.0.0.1:8000/measures/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measures/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})