from django.contrib import admin
# the module name is app_name.models
from version3.models import Chofer, Contrato, Barrio, Chofer_Barrio, Colegio, Tarifa
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
class ChoferAdmin(admin.ModelAdmin):
	list_display = ['id_chofer', 'nombre_chofer','email_chofer', 'pass_chofer']
admin.site.register(Chofer, ChoferAdmin)

class ContratoAdmin(admin.ModelAdmin):
	list_display = ['id_contrato', 'id_chofer', 'id_usuario', 'estado', 'direccion', 'barrio', 'destino', 'cant_asientos', 'comentarios']
admin.site.register(Contrato, ContratoAdmin)

class Barrio_Admin(admin.ModelAdmin):
	list_display = ['id_barrio', 'nombre_barrio', 'ubicacion']
admin.site.register(Barrio, Barrio_Admin)

class Chofer_Barrio_Admin(admin.ModelAdmin):
	list_display = ['id_chofer', 'id_barrio']
admin.site.register(Chofer_Barrio, Chofer_Barrio_Admin)

class Colegio_Admin(admin.ModelAdmin):
	list_display = ['id_colegio', 'nombre_colegio', 'direccion_colegio']
admin.site.register(Colegio, Colegio_Admin)

class Tarifa_Admin(admin.ModelAdmin):
	list_display = ['id_barrio', 'id_colegio', 'precio']
admin.site.register(Tarifa, Tarifa_Admin)
