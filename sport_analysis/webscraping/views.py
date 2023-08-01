from django.shortcuts import render
from django.http import HttpResponse
from .main.ws_basketball import catch_data_leagues
from .main.test_match import get_and_set_data_basketaball
from .main.search_links_basketball import get_links


# Create your views here.
def ws_basketball_view(request):
    catch_data_leagues()

    # Después de realizar el webscraping y guardar los datos en la base de datos, puedes mostrar un mensaje
    return HttpResponse("Webscraping completado y datos guardados en la base de datos.")


def test_match_view(request):
    get_and_set_data_basketaball()

    return HttpResponse('TEST!!!.....')


def searc_links_view(request):
    get_links()

    return HttpResponse('Links Ok!!!')