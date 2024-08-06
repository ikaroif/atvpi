from django.urls import path
from .views import ikaro_view

urlpatterns = [
    path('ikaro/', ikaro_view),
]
