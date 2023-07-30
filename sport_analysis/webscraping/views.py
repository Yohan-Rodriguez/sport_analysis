from django.shortcuts import render
from django.http import HttpResponse
from .ws_basketball import catch_data_leagues


# Create your views here.
def ws_basketball_view(request):
    catch_data_leagues()

    # Después de realizar el webscraping y guardar los datos en la base de datos, puedes mostrar un mensaje
    return HttpResponse("Webscraping completado y datos guardados en la base de datos.")
