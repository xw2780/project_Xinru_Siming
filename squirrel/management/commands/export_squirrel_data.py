import csv
import datetime
from django.core.management.base import BaseCommand
from squirrel.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        with open(options['path'],'w') as fp:
            writer = csv.DictWriter(
                    fp, 
                    delimiter=',',
                    fieldnames=[
                        'X',
                        'Y',
                        'Unique Squirrel ID',
                        'Shift',
                        'Date',
                        'Age',
                        'Primary Fur Color',
                        'Location',
                        'Specific Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail flags',
                        'Tail twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs from'
                        ]
                    )
            writer.writeheader()
    
            for row in Squirrel.objects.all():
                if row.date: 
                    the_date = row.date.strftime('%m%d%Y')
                else:
                    the_date = row.date

                writer.writerow({
                    'X':row.longitude,
                    'Y':row.latitude,
                    'Unique Squirrel ID':row.unique_squirrel_id,
                    'Shift':row.shift,
                    'Date':the_date,
                    'Age':row.age,
                    'Primary Fur Color':row.primary_color,
                    'Location':row.location,
                    'Specific Location':row.specific_location,
                    'Running':row.running,
                    'Chasing':row.chasing,
                    'Climbing':row.climbing,
                    'Eating':row.eating,
                    'Foraging':row.foraging,
                    'Other Activities':row.other_activities,
                    'Kuks':row.kuks,
                    'Quaas':row.quaas,
                    'Moans':row.moans,
                    'Tail flags':row.tail_flags,
                    'Tail twitches':row.tail_twitches,
                    'Approaches':row.approaches,
                    'Indifferent':row.indifferent,
                    'Runs from':row.runs_from,          
                    })
