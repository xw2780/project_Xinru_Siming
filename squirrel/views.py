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
            }
    return render(request, 'squirrel/sightings.html', context)

def map_view(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels':squirrels,
            }
    return render(request, 'squirrel/map.html', context)




def add_view(request):
    squirrels = Squirrel.objects.all()
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('squirrel/sightings.html')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SquirrelForm()

    context = {
            'form':form,
            }
    return render(request, 'squirrel/add.html', context)

def stats_view(request):
    squirrels = Squirrel.objects.all()
    #total # of records
    n = squirrels.count()
    #shift
    AM_n = squirrels.filter(shift='AM').count()
    PM_n = squirrels.filter(Shift='PM').count()
    AM_pct = AM_n/n
    AM_pct = "{:.2%}".format(AM_pct)
    PM_pct = PM_n/n
    PM_pct = "{:.2%}".format(PM_pct)
    #age
    Juvenile_n = squirrels.filter(age='juvenile').count()
    Adult_n = squirrels.filter(age='adult').count()
    Juvenile_pct = Juvenile_n/n
    Juvenile_pct = "{:.2%}".format(Juvenile_pct)
    Adult_pct = Adult_n/n
    Adult_pct = "{:.2%}".format(Adult_pct)
    #primary_fur_color
    Black_n = squirrels.filter(primary_color='Black').count()
    Gray_n = squirrels.filter(primary_color='Gray').count()
    Cinnamon_n = squirrels.filter(primary_color='Cinnamon').count()
    Black_pct = Black_n/n
    Black_pct = "{:.2%}".format(Black_pct)
    Gray_pct = Gray_n/n
    Gray_pct = "{:.2%}".format(Gray_pct)
    Cinnamon_pct = Cinnamon_n/n
    Cinnamon_pct = "{:.2%}".format(Cinnamon_pct)
    #location
    Above_Ground_n = squirrels.filter(location='Above_ground').count()
    Ground_Plane_n = squirrels.filter(location='Ground_plane').count()
    Above_Ground_pct = Above_Ground_n/n
    Above_Ground_pct = "{:.2%}".format(Above_Ground_pct)
    Ground_Plane_pct = Ground_Plane_n/Ground_plane
    Ground_Plane_pct= "{:.2%}".format(Ground_Plane_pct)
    #movement
    Approaches_pct = squirrels.filter(approaches=True).count()/n
    Indifferent_pct = squirrels.filter(indifferent=True).count()/n
    Runs_From_pct = squirrels.filter(runs_from=True).count()/n
    Approaches_pct = "{:.2%}".format(Approaches_pct)
    Indifferent_pct = "{:.2%}".format(Indifferent_pct)
    Runs_From_pct ="{:.2%}".format(Runs_From_pct)
    
    context = {
            'Total':n,
            'Shift': {'AM': AM_n,'PM': PM_n},
            'Shift_pct': {'AM': AM_pct,'PM': PM_pct},
            'Age': {'Juvenile': Juvenile_n, 'Adult': Adult_n},
            'Age_pct': {'Juvenile': Juvenile_pct, 'Adult': Adult_pct},
            'Primary_Fur_Color': {'Black':Black_n, 'Gray':Gray_n, 'Cinnamon':Cinnamon_n},
            'Primary_Fur_Color_pct': {'Black':Black_pct, 'Gray':Gray_pct, 'Cinnamon':Cinnamon_pct},
            'Location': {'Above_Ground':Above_Ground_n, 'Ground_Plane':Ground_Plane_n},
            'Location_pct': {'Above_Ground':Above_Ground_pct, 'Ground_Plane':Ground_Plane_pct},
            'Movements': {'Approaches_pct':Approaches_pct, 'Indifferent_pct':Indifferent_pct,'Runs_From_pct':Runs_From_pct},
            }

    return render(request, 'squirrel/sightings/stats.html', context)



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

