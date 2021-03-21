# serializers.py
from rest_framework import serializers

from .models import Chofer

class ChoferSerializer (serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Chofer
        fields = ('id_chofer', 'nombre_chofer', 'email_chofer', 'pass_chofer')