from django.shortcuts import render

# Create your views here.
from menu.models import MenuHeader


def index(request):
    return render(request, 'menu/index.html', context={'headers': MenuHeader.objects.all()})


def draw_menu(request, path):
    splitted_path = path.split('/')
    return render(
        request, 'menu/index.html', context={'header': splitted_path[0], 'item': splitted_path[-1]})