from django.urls import path

from . import views

urlpatterns = [
        path('',views.homepage_view),
        path('sightings/',views.sightings_view),
        path('map/',views.map_view),
        path('sightings/<unique_squirrel_id>/',views.update_view),
        path('sightings/add/',views.add_view),
        path('sightings/stats/',views.stats_view),
        ]
