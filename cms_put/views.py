from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from models import Pages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def id (request , identificador ):
    try :
        pages = Pages.objects.get(id = int(identificador)) #me muestra el id
        pag = str(pages.page)
        return HttpResponse ('<h1>Todo correcto<h2>'+ str(pages))
    except Pages.DoesNotExist :
        respuesta = ("<h1>Error . No hay pagina para este identificador </h1>")
        return HttpResponse(respuesta)

def mostrar (request , recurso) :
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pages in lista :
        respuesta += '<li><a href = "'+ str(pages.id) +'" >' + pages.nombre + '</a>'
        respuesta += '</ol>'
    return HttpResponse (respuesta)

@csrf_exempt

def uso_put (request , nombre , cuerpo):
    if request.method == 'GET':
        page_new = Pages (nombre = nombre , page = cuerpo)
        page_new.save()
    elif request.method == 'PUT' or request.method == 'POST' :
        page_new = Pages (nombre = nombre , page = request.body)
        page_new.save()

    return HttpResponse ('Pagina introducidad')
