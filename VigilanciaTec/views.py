from django.http import HttpResponse
import datetime
from django.shortcuts import render

#Creación de vista-Código Python
def saludo(request):
    documento = """<html>
    <body>
    <h1>HERRAMIENTA DE VIGILANCIA TECNOLÓGICA
    </h1>
    </body>
    </html>"""
    
    return HttpResponse(documento)

#Formulario para el envio de datos

def busqueda(request):
    return render(request, "busqueda_articulos.html")
    