from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):

    longitude = models.FloatField(help_text = _('Longitude of the sight'),)
    
    latitude = models.FloatField(help_text = _('Latitude of the sight'),)
    
    unique_squirrel_id = models.CharField(
            help_text = _('The unique ID of the squirrel'),
            max_length = 50,
            )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [
            (AM, _('AM')),
            (PM, _('PM')),
    ]
    shift = models.CharField(
            max_length = 4,
            help_text = _('Shift of Sightings'),
            choices = SHIFT_CHOICES,
            blank=True,
    )

    date = models.DateField(
            help_text = _('Date of sighting'),
            blank = True,
            null = True,
    )
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'
    AGE_CHOICES = (
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (Unknown, '?'),
            )
    age = models.CharField(
            max_length = 50,
            help_text = _('Age of squirrel'),
            choices = AGE_CHOICES,
            blank = True,
    )

    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    COLOR_CHOICES = (
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
     )
    primary_color = models.CharField(
            max_length = 50,
            help_text = _('Fur color of squirrel'),
            choices = COLOR_CHOICES,
            blank = True,
    )
    
    Ground_plane = 'ground plane'
    Above_ground = 'above ground'
    LOCATION_CHOICES = (
            (Ground_plane,'Ground Plane'),
            (Above_ground,'Above Ground'),
    )        
    location = models.CharField(
            max_length = 50,
            help_text = _('location of sighting'),
            choices = LOCATION_CHOICES,
            blank = True,
    )

    specific_location = models.TextField(
            help_text = _('Additional information about location'),
            blank = True,
    )

    running = models.BooleanField(
            help_text = _('Whether the squirrel is running'),
    )

    chasing = models.BooleanField(
            help_text = _('Whether the squirrel is chasing'),
    )

    climbing = models.BooleanField(
            help_text = _('Whether the squirrel is climbing'),
    )

    eating = models.BooleanField(
            help_text = _('Whether the squirrel is eating'),
    )

    foraging = models.BooleanField(
            help_text = _('Whether the squirrel is foraging'),
    )

    other_activities = models.TextField(
            help_text = _('Additional information about activities'),
            blank = True,
    )

    kuks = models.BooleanField(
            help_text = _('Whether the squirrel kuks'),
    )

    quaas = models.BooleanField(
            help_text = _('Whether the squirrel quaas'),
    )

    moans = models.BooleanField(
            help_text = _('Whether the squirrel is moans'),
    )

    tail_flags = models.BooleanField(
            help_text = _('Whether the squirrel has flag tail'),
    )

    tail_twitches = models.BooleanField(
            help_text = _('Whether the squirrel has twithced tail'),
    )

    approaches = models.BooleanField(
            help_text = _('Whether the squirrel approaches people'),
    )

    indifferent = models.BooleanField(
            help_text = _('Whether the squirrel is indifferent to people'),
    )
    runs_from = models.BooleanField(
            help_text = _('Whether the squirrel runs from  people'),
    )

