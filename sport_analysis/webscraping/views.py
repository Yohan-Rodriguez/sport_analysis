from django.http import HttpResponse
from webscraping.main.nba.ws_nba import get_and_set_data_nba


def ws_nba(request):
    get_and_set_data_nba()

    return HttpResponse('NBA TEST!')

