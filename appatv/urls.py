from django.urls import path
from .views import ikaro_view, davis_view

urlpatterns = [
    path('ikaro/', ikaro_view),
    path('davis/', davis_view)
]
