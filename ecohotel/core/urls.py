from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_data, name="show_data"),
    path('data', views.energy_produced_consumed, name="energy_produced_consumed"),
    path('totals', views.show_totals, name="show_totals"),
]