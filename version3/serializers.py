# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Chofer, Contrato

class ChoferSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Chofer
        fields = ('id_chofer', 'nombre_chofer', 'email_chofer', 'pass_chofer')

class ContratoSerializer(serializers.HyperlinkedModelSerializer):
	# choferes = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
	class Meta: 
		model = Contrato
		fields = ('id_contrato', 'id_usuario', 'direccion', 'barrio', 'destino', 'cant_asientos', 'estado', 'comentarios', 'fecha', 'hora' , 'telefono')
		
class UserSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = User
        fields = ('id', 'username', 'email')
