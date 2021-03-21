from django.db import models
from django.urls import reverse

class Barrio(models.Model):
	id_barrio = models.AutoField(primary_key=True)
	nombre_barrio = models.CharField(max_length=120)
	ubicacion = models.TextField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'barrios'

	def __unicode__(self):
		return u"%s's Barrios Info" % self.id_barrio

	def __str__(self):
		return self.nombre_barrio


class Chofer_Barrio(models.Model):
	id_chofer = models.ForeignKey('Chofer', on_delete=models.CASCADE)
	id_barrio = models.IntegerField(null=False)

	class Meta:
		verbose_name_plural = 'choferes_barrio'
		unique_together = (('id_chofer', 'id_barrio'),)

	def __unicode__(self):
		return u"%s's Choferes_Barrio Info" % self.id_chofer

class Chofer(models.Model):
	id_chofer = models.AutoField(primary_key=True)
	nombre_chofer = models.CharField(max_length=120)
	calif_chofer = models.IntegerField(default=3)
	description_chofer = models.TextField(null=True, blank=True)
	email_chofer = models.CharField(max_length=120, default='eberuruguay@gmail.com')
	pass_chofer = models.CharField(max_length=16, null=False, default='1234')

	class Meta:
		verbose_name_plural = 'choferes'

	def __unicode__(self):
		return u"%s's choferes info" % self.id_chofer

	def __str__(self):
		return self.nombre_chofer

class Contrato(models.Model):
	id_contrato = models.AutoField(primary_key=True)
	id_chofer = models.ForeignKey('Chofer', on_delete=models.CASCADE)
	id_usuario = models.CharField(max_length=60, null=False)
	direccion = models.CharField(max_length=120, null=True)
	barrio = models.CharField(max_length=120)
	destino = models.CharField(max_length=120)
	cant_asientos = models.IntegerField(null=False)
	estado = models.IntegerField(default=0)
	comentarios = models.TextField(null=True, blank=True)
	fecha = models.CharField(null=False, max_length=20, default='2020-03-11')
	hora = models.CharField(null=False, max_length=10, default='07:00')

	class Meta:
		verbose_name_plural = 'contratos'

	def __unicode__(self):
		return u"%s's Contratos Info" % self.id_contrato

class Colegio(models.Model):
	id_colegio = models.AutoField(primary_key=True)
	nombre_colegio = models.CharField(max_length=120)
	direccion_colegio = models.TextField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'colegios'

	def __unicode__(self):
		return u"%s's colegios Info" % self.id_colegio

	def __str__(self):
		return self.nombre_colegio

class Tarifa(models.Model):
	id_barrio = models.ForeignKey('Barrio', on_delete=models.CASCADE)
	id_colegio = models.ForeignKey('Colegio', on_delete=models.CASCADE)
	precio = models.IntegerField(null=False)

	class Meta:
		verbose_name_plural = 'tarifas'

	def __unicode__(self):
		return u"%s's tarifas Info" % self.id_colegio
