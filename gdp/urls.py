from rest_framework.urls import path
from . import views

urlpatterns = [
    path('gdp', views.GdpApi.as_view()),
    path('chart', views.GdpChartApi.as_view()),
]