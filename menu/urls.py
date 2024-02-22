from django.urls import path
from menu.views import index, draw_menu

urlpatterns = [
    path('', index, name='headers'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
