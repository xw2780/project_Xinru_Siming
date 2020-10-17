from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
import pandas as pd
import numpy as n
from datetime import date,datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from .models import Squirrel
from .forms import SquirrelForm

# Create your views here.
def homepage_view(request):
    return render(request, 'squirrel/homepage.html')

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

def update_view(request,unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect('squirrel/sightings.html')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SquirrelForm(instance = squirrel)

    context = {
            'form':form,
            }
    return render(request, 'squirrel/update.html', context)

