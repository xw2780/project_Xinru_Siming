# Generated by Django 3.0.7 on 2020-10-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(help_text='Longitude of the sight')),
                ('latitude', models.FloatField(help_text='Latitude of the sight')),
                ('unique_squirrel_id', models.CharField(help_text='The unique ID of the squirrel', max_length=50)),
                ('shift', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift of Sightings', max_length=4)),
                ('date', models.DateField(blank=True, help_text='Date of sighting', null=True)),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?')], help_text='Age of squirrel', max_length=50)),
                ('primary_color', models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon')], help_text='Fur color of squirrel', max_length=50)),
                ('location', models.CharField(blank=True, choices=[('ground plane', 'Ground Plane'), ('above ground', 'Above Ground')], help_text='location of sighting', max_length=50)),
                ('specific_location', models.TextField(blank=True, help_text='Additional information about location')),
                ('running', models.BooleanField(help_text='Whether the squirrel is running')),
                ('chasing', models.BooleanField(help_text='Whether the squirrel is chasing')),
                ('climbing', models.BooleanField(help_text='Whether the squirrel is climbing')),
                ('eating', models.BooleanField(help_text='Whether the squirrel is eating')),
                ('foraging', models.BooleanField(help_text='Whether the squirrel is foraging')),
                ('other_activities', models.TextField(blank=True, help_text='Additional information about activities')),
                ('kuks', models.BooleanField(help_text='Whether the squirrel kuks')),
                ('quaas', models.BooleanField(help_text='Whether the squirrel quaas')),
                ('moans', models.BooleanField(help_text='Whether the squirrel is moans')),
                ('tail_flags', models.BooleanField(help_text='Whether the squirrel has flag tail')),
                ('tail_twitches', models.BooleanField(help_text='Whether the squirrel has twithced tail')),
                ('approaches', models.BooleanField(help_text='Whether the squirrel approaches people')),
                ('indifferent', models.BooleanField(help_text='Whether the squirrel is indifferent to people')),
                ('runs_from', models.BooleanField(help_text='Whether the squirrel runs from  people')),
            ],
        ),
    ]
