from django.forms import ModelForm
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
       # fields = '__all__'
        fields = ['latitude','longitude','unique_squirrel_id','shift','date','age']

class SquirrelFormAll(ModelForm):
    class Meta:
        model = Squirrel 
        fields = '__all__'
