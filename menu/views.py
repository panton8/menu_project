from django.shortcuts import render

# Create your views here.
from menu.models import MenuHeader


def index(request):
    return render(request, 'menu/index.html', context={'headers': MenuHeader.objects.all()})
