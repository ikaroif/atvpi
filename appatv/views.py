from django.shortcuts import render
from django.http import HttpResponse

def ikaro_view(request):
    return HttpResponse("Autor: Íkaro")
