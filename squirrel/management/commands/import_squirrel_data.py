import csv
from  django.core.management.base import BaseCommand
import datetime
from squirrel.models import Squirrel

def convertBool(s):
    if s.lower() == "true":
        return True
    else:
        return False
    
class Command(BaseCommand):
    help = 'Import squirrel sightings data'
    def add_arguments(self,parser):
        parser.add_argument('squirrel_data', help='file of squirrel data')
    def handle(self, *args, **options):
        file_ = options['squirrel_data']
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                if row['Age'] not in ['Adult', 'Juvenile']:
                    s_age = ''
                elif row['Age'] == 'Adult':
                    s_age = Squirrel.Adult
                elif row['Age'] == 'Juvenile':
                    s_age = Squirrel.Juvenile
                if row['Primary Fur Color'] not in ['Gray', 'Cinnamon','Black']:
                    s_color = ''
                elif row['Primary Fur Color'] == 'Gray':
                    s_color = Squirrel.Gray
                elif row['Primary Fur Color'] == 'Cinnamon':
                    s_color = Squirrel.Cinnamon          
                elif row['Primary Fur Color'] == 'Black':
                    s_color = Squirrel.Black
                if row['Location'] not in ['Ground Plane', 'Above Ground']:
                    s_location = ''
                elif row['Location'] == 'Ground Plane':
                    s_location = Squirrel.Ground_plane
                elif row['Location'] == 'Above Ground':
                    s_location = Squirrel.Above_ground
                    
                s = Squirrel(
                    longitude = row['X'],
                    latitude = row['Y'],
                    unique_squirrel_id = row['Unique Squirrel ID'],
                    shift = row['Shift'],
                    date = datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                    age = s_age,
                    primary_color = s_color,
                    location = s_location,
                    specific_location = row['Specific Location'],
                    running = convertBool(row['Running']),
                    chasing = convertBool(row['Chasing']),
                    climbing = convertBool(row['Climbing']),
                    eating = convertBool(row['Eating']),
                    foraging = convertBool(row['Foraging']),
                    other_activities = row['Other Activities'],
                    kuks = convertBool(row['Kuks']),
                    quaas = convertBool(row['Quaas']),
                    moans = convertBool(row['Moans']),
                    tail_flags = convertBool(row['Tail flags']),
                    tail_twitches = convertBool(row['Tail twitches']),
                    approaches = convertBool(row['Approaches']),
                    indifferent = convertBool(row['Indifferent']),
                    runs_from = convertBool(row['Runs from']),
                    )
                s.save()
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))

