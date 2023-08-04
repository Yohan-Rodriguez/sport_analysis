from django.shortcuts import render
from django.http import HttpResponse
from .main.search_links_basketball import get_links
from .main.ws_basketball import get_and_set_data_basketaball
from .main.ws_basketball_test import test_get_and_set_data_basketaball
from .main.test_match import test



# Create your views here.
def ws_basketball_view(request):
    get_and_set_data_basketaball()

    # Después de realizar el webscraping y guardar los datos en la base de datos, puedes mostrar un mensaje
    return HttpResponse("Webscraping completado y datos guardados en la base de datos.")



def ws_basketball_test_view(request):
    test_get_and_set_data_basketaball()
    
    return HttpResponse('"test_catch_data_leagues()" !!!...')



def test_match_view(request):
    test()

    return HttpResponse('TEST!!!.....')



def searc_links_view(request):
    get_links()

    return HttpResponse('Links Ok!!!')