from django.shortcuts import render
import json
import pandas as pd
import numpy as n
from datetime import date,datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Squirrel
# Create your views here.
def sightings_view(request):
    squirrels = Squirrel.objects.all()
    fields = ['unique_squirrel_id','longtitude','latitude','date']
    context = {
            'squirrels':squirrels,
            'fields':fields,
            }
    return render(request, 'squirrel/sightings.html', context)

def map_view(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels':squirrels,
            }
    return render(request, 'squirrel/map.html', context)

