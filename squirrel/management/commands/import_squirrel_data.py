import csv
from  django.core.management.base import BaseCommand
import datetime
from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel sightings data'

    def add_arguments(self,parser):
        parser.add_argument('squirrel_data', help='file of squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_data']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for row in reader:
                try:
                        _, created = Squirrel.objects.get_or_create(
                            latitude=float(row[0]),
                            longitude=float(row[1]),
                            unique_squirrel_id=row[2],
                            shift=row[4],
                            date=datetime.date(int(row[5][-4:]),int(row[5][0:2]),int(row[5][2:4])),
                            age=row[7], 
                            primary_color=row[8],
                            location=row[12],
                            specific_location=row[14],
                            running=str_bool(row[15]),
                            chasing=str_bool(row[16]),
                            climbing=str_bool(row[17]),
                            eating=str_bool(row[18]),
                            foraging=str_bool(row[19]),
                            other_activities=row[20],
                            kuks=str_bool(row[21]),
                            quaas=str_bool(row[22]),
                            moans=str_bool(row[23]),
                            tail_flags=str_bool(row[24]),
                            tail_twitches=str_bool(row[25]),
                            approaches=str_bool(row[26]),
                            indifferent=str_bool(row[27]),
                            runs_from=str_bool(row[28])
                        )
                    except:
                        pass

        msg = f'You are importing from {file_}'
        self.stdout.write(self.stype.SUCCESS(msg))


