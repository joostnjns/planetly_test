from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q   # To do the logical OR filter in view
from django.template import loader
from api_test.models import TemperaturesByCity
from rest_framework import generics
from .serializers import  TempyByCitySerializer

# Create your views here.
def top_n(request, n, start, end):
    if request.method == 'GET':
        # For now only return start or end year
        top_cities = TemperaturesByCity.objects.order_by('-averagetemperature').filter(year__gte= start, year__lte = end)[:n]
        context = {"top_cities": top_cities}
        return render(request, "cities_detail.html", context)

class TempByCityCreate(generics.CreateAPIView):
    # API endpoint for creation of new entries
    queryset = TemperaturesByCity.objects.all(),
    serializer_class = TempyByCitySerializer

class TempByCityDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single row by id
    queryset = TemperaturesByCity.objects.all()
    serializer_class = TempyByCitySerializer

class TempByCityUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a record to be updated
    queryset = TemperaturesByCity.objects.all()
    serializer_class = TempyByCitySerializer

class TempByCityDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a record to be deleted
    queryset = TemperaturesByCity.objects.all()
    serializer_class = TempyByCitySerializer


#top_records = TemperaturesByCity.objects.order_by('averagetemperature').filter( Q(TemperaturesByCity.dt.startswith(str(start)) | TemperaturesByCity.dt.startswith(str(end))))[:n]