from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .models import Chofer, Contrato, Chofer_Barrio, Barrio, Colegio, Tarifa
from django.core.mail import send_mail
from .forms import UserCreationForm, ModificationForm
from django.contrib.auth.models import User

from rest_framework import viewsets 

from .serializers import ChoferSerializer, ContratoSerializer
from .models import Chofer
from rest_framework.generics import(ListCreateAPIView)

def buscarchofer(request):
	if request.method == "POST":
		datos_choferes = Chofer.objects.filter(chofer_barrio__id_barrio=request.POST.get('barrio'))
		#datos_choferes = id_choferes_barrio.all()
		tarifas = Tarifa.objects.get(id_colegio = request.POST.get('colegio'), id_barrio = request.POST.get('barrio'))
		datos_barrio = Barrio.objects.get(id_barrio=request.POST.get('barrio'))
		datos_colegio = Colegio.objects.get(id_colegio=request.POST.get('colegio'))

		num_asientos = request.POST.get('asientos')
		if num_asientos is not None and num_asientos.isnumeric():
			condition = {}
			condition['num_asientos'] = int(num_asientos)

		tarifaxasiento = tarifas.precio * condition['num_asientos']
		
		#DIRECCIONES de PRUEBA
		colegio_seminario = "!4m5!1s0x959f812d1ae755a3%3A0x187dfc95ca170be7!2scolegio%20Seminario%2C%20Soriano%2C%20Montevideo%2C%20Soriano%201570%2C%2011200%20Montevideo%2C%20Departamento%20de%20Montevideo!3m2!1d-34.9072229!2d-56.1825839!5e0!3m2!1ses!2suy!4v1584059154265!5m2!1ses!2suy"
		colegio_elbiofernandez = "!4m5!1s0x959f81cbe1ecb0dd%3A0x36abf39686a5bfb3!2sEscuela%20y%20Liceo%20Elbio%20Fern%C3%A1ndez%2C%20Canelones%2C%20Montevideo%20Departamento%20de%20Montevideo!3m2!1d-34.9089671!2d-56.1858698!5e0!3m2!1ses!2suy!4v1584059864934!5m2!1ses!2suy"
		colegio_maristas = "!4m5!1s0x959f80f9d61bded7%3A0x7d8ae24da5e16cec!2sColegio%20y%20Liceo%20Santa%20Mar%C3%ADa%20Hermanos%20Maristas%2C%20Avenida%208%20de%20Octubre%2C%20Montevideo%20Departamento%20de%20Montevideo!3m2!1d-34.8850327!2d-56.1555554!5e0!3m2!1ses!2suy!4v1584060046366!5m2!1ses!2suy"
		barrio_tres_cruces = "1d13090.319695660375!2d-56.171537972496694!3d-34.89189348617109!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x959f8051b30d290f%3A0xafa4443090520bbc!2sTres%20Cruces%2C%20Montevideo%20Departamento%20de%20Montevideo!3m2!1d-34.8949581!2d-56.168640399999994"
		barrio_la_teja = "1d52374.22108559094!2d-56.23270004747067!3d-34.87158147990411!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x95a1d5688daffea7%3A0x9e4374837096cbe5!2sLa%20Teja%2C%20Montevideo%20Departamento%20de%20Montevideo!3m2!1d-34.8586431!2d-56.238859999999995"
		barrio_cordon = "1d13089.842925820718!2d-56.17775287249519!3d-34.89488563615904!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x959f804b61dd87fb%3A0xa618115bb8074eb6!2sCord%C3%B3n%2C%20Montevideo%20Departamento%20de%20Montevideo!3m2!1d-34.9041401!2d-56.1784106"

		context = {
			"datos_tarifa": tarifaxasiento,
			"barrio": request.POST.get('barrio'),
			"direccion": request.POST.get('direccion'),
			"asientos": request.POST.get('asientos'),
			"colegio": request.POST.get('colegio'),
			"fecha": request.POST.get('fecha'),
			"hora": request.POST.get('hora'),
			"datos_choferes": datos_choferes,
			"datos_barrio": datos_barrio,
			"datos_colegio": datos_colegio,
			"colegio_seminario": colegio_seminario,
			"colegio_elbiofernandez": colegio_elbiofernandez,
			"colegio_maristas": colegio_maristas,
			"barrio_tres_cruces": barrio_tres_cruces,
			"barrio_la_teja": barrio_la_teja,
			"barrio_cordon": barrio_cordon,
		}
		return render(request, "mostrar_choferes.html", context)
	else:
		barrios = Barrio.objects.all()
		colegios = Colegio.objects.all()
		context = {
			"datos_colegios": colegios,
			"datos_barrios": barrios
		}
		return render(request, "buscar_chofer.html", context)


def misdatos(request):
	form = ModificationForm(instance=request.user)
	if request.method =="POST":
		form = ModificationForm(data=request.POST, instance=request.user)
		if form.is_valid():
			user = form.save()
			from django.contrib import messages
			messages.success(request, 'Datos de perfil actualizados.')
		else:
			form = ModificationForm(instance=request.user)
	return render(request, "mis_datos.html", {'form':form})

def finalizar(request):
	queryset = Chofer.objects.filter(id_chofer = request.POST.get('id_chofer1')).values()
	contrato = Contrato.objects.filter(id_contrato = request.POST.get('id_contrato')).values()
	context = {
		"id_contrato": contrato,
		"datos_chofer": queryset
	}
	return render(request, "calif_chofer.html", context)

def cancelar_c(request):
	if request.POST.get('estrellas') == None:
		calificacion = '0'
	else:
		calificacion = request.POST.get('estrellas')

	contrato = Contrato.objects.filter(id_contrato = request.POST.get('id_contrato')).first()
	#send_mail('title', 'Se han cancedo %s Asientos para la direccion: %s con destino: %s' % (request.POST.get('cant_asientos'), request.POST.get('direccion'), request.POST.get('destino')), 'eberuruguay@gmail.com', [request.POST.get('email_chofer')], fail_silently=False)
	send_mail('Finalizado', 'Se ha calificado con %s estrella/s el viaje de %s asiento/s para la direccion: %s con destino: %s. Fecha: %s. Hora: %s. Comentarios: %s' % (calificacion, contrato.cant_asientos, contrato.direccion, contrato.destino, contrato.fecha, contrato.hora, request.POST.get('comentarios')), 'eberuruguay@gmail.com', [request.POST.get('email_chofer')], fail_silently=False)
	send_mail('Finalizado', 'Se ha calificado con %s estrella/s el viaje de %s asiento/s para la direccion: %s con destino: %s. Fecha: %s. Hora: %s. Comentarios: %s' % (calificacion, contrato.cant_asientos, contrato.direccion, contrato.destino, contrato.fecha, contrato.hora, request.POST.get('comentarios')), 'eberuruguay@gmail.com', [request.user.email], fail_silently=False)
	#send_mail('title', 'Se han cancedo %s Asientos para la direccion: %s con destino: %s' % (request.POST.get('cant_asientos'), request.POST.get('direccion'), request.POST.get('destino')), 'eberuruguay@gmail.com', [request.user.email], fail_silently=False)
	Contrato.objects.filter(id_contrato = request.POST.get('id_contrato')).delete()
	return redirect('/mischoferes')

def mis_choferes(request):
	queryset = Contrato.objects.filter(id_usuario = request.user.id)
	context = {
		"contratos_list": queryset
	}
	return render(request, "mis_choferes.html", context)


def contratar(request):
	direccion=request.POST.get('direccion')
	barrio=request.POST.get('barrio')
	destino=request.POST.get('colegio')
	cant_asientos=request.POST.get('asientos')
	comentarios=request.POST.get('comentarios')
	telefono=request.POST.get('telefono')
	tarifa=request.POST.get('tarifa')
	fecha=request.POST.get('fecha')
	hora=request.POST.get('hora')
	contrato1 = Contrato(
	id_chofer=get_object_or_404(Chofer, id_chofer=request.POST.get('id_chofer1')),
	id_usuario=request.user.id,
	fecha=fecha,
	hora=hora,
	direccion=direccion,
	barrio=barrio,
	destino=destino,
	cant_asientos=cant_asientos,
	comentarios=comentarios,
	telefono=telefono,
	estado=1)
	contrato1.save()
	datos_chofer=Chofer.objects.get(id_chofer=request.POST.get('id_chofer1'))
	#[request.POST.get('email_chofer')]
	send_mail('Contratado', 'Se ha/n contratado %s asiento/s para la direccion: %s con destino: %s. Fecha: %s. Hora: %s. A cargo de: %s. Tarifa: $%s. Comentarios: %s' % (cant_asientos, direccion, destino, fecha, hora, datos_chofer.nombre_chofer, tarifa, comentarios), 'eberuruguay@gmail.com', [request.POST.get('email_chofer')], fail_silently=False)
	send_mail('Contratado', 'Se ha/n contratado %s asiento/s para la direccion: %s con destino: %s. Fecha: %s. Hora: %s. A cargo de: %s. Tarifa: $%s. Comentarios: %s' % (cant_asientos, direccion, destino, fecha, hora, datos_chofer.nombre_chofer, tarifa, comentarios), 'eberuruguay@gmail.com', [request.user.email], fail_silently=False)
	return render(request, "contrato.html")

def list_choferes(request):
		queryset = Chofer.objects.all()
		context = {
			"chofer_list": queryset
			}
		return render(request, "choferes.html", context)

def datos_chofer(request):
	queryset = Chofer.objects.filter(id_chofer = request.GET.get('id')).values()
	context = {
		"datos_chofer": queryset
	}
	return render(request, "datos_chofer.html", context)

def welcome(request):
	if request.user.is_authenticated:
		return render(request, "welcome.html")
	else:
		return redirect('/login')

def register(request):
	# Creamos el formulario de autenticación vacío
	form = UserCreationForm()
	if request.method == "POST":
		# Añadimos los datos recibidos al formulario
		form = UserCreationForm(data=request.POST)
		# Si el formulario es válido...
		if form.is_valid():

			# Creamos la nueva cuenta de usuario
			user = form.save()

			# Si el usuario se crea correctamente
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('/')

	# Si queremos borramos los campos de ayuda
	form.fields['username'].help_text = None
	form.fields['password1'].help_text = None
	form.fields['password2'].help_text = None

	# Si llegamos al final renderizamos el formulario
	return render(request, "register.html", {'form': form})

def login(request):
	# Creamos el formulario de autenticación vacío
	form = AuthenticationForm()
	if request.method == "POST":
		# Añadimos los datos recibidos al formulario
		form = AuthenticationForm(data=request.POST)
		# Si el formulario es válido...
		if form.is_valid():
			# Recuperamos las credenciales validadas
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			# Verificamos las credenciales del usuario
			user = authenticate(username=username, password=password)

			# Si existe un usuario con ese nombre y contraseña
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('/')

	# Si llegamos al final renderizamos el formulario
	return render(request, "login.html", {'form': form})

def logout(request):
	# Finalizamos la sesión
	do_logout(request)
	# Redireccionamos a la portada
	return redirect('/')



class ChoferLoginViewSet (ListCreateAPIView): 
     
    serializer_class = ChoferSerializer
    def get_queryset(self): 
    	em= self.request.GET.get('em')
    	ps= self.request.GET.get('ps')
    	chofer = Chofer.objects.filter(email_chofer= em, pass_chofer= ps)
    	return chofer

class ChoferViajesViewSet (viewsets.ModelViewSet): 
    serializer_class = ContratoSerializer
    def get_queryset(self): 
    	
    	id_chofer= self.request.GET.get('id')
    	viajes = Contrato.objects.filter(id_chofer= id_chofer, estado = 1)
    	return viajes

def finalizar_viaje(request):
	contrato = Contrato.objects.filter(id_contrato =request.GET.get('contrato'), id_chofer = request.GET.get('chofer')).update(estado=0)
	return redirect('/')

class ChoferViajesViewSet2 (viewsets.ModelViewSet):     
    serializer_class = ContratoSerializer
    def get_queryset(self): 
    	
    	id_chofer= self.request.GET.get('id')
    	viajes = Contrato.objects.filter(id_chofer= id_chofer, estado = 0)
    	return viajes
