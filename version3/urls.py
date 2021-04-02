"""version3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from version3 import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import include
from .views import *

urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
	path('choferes', views.list_choferes),
    path('admin/', admin.site.urls),
	path('datoschofer', views.datos_chofer),
	path('contratar', views.contratar, name="contratar"),
	path('mischoferes', views.mis_choferes),
	path('cancelar', views.cancelar_c, name="cancelar"),
	path('misdatos', views.misdatos),
	path('reset-password', PasswordResetView.as_view(), name='password_reset'),
	path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset-password/complete/', PasswordResetCompleteView.as_view(),name='password_reset_complete'),
	path('buscarchofer', views.buscarchofer, name="buscarchofer"),
	path('mostrarchoferes', views.buscarchofer, name="mostrarchoferes"),
	path('finalizar', views.finalizar, name="finalizar"),
	path('loginchofer', ChoferLoginViewSet.as_view(), name='loginchofer'),
	path('viajeschofer', ChoferViajesViewSet.as_view({'get': 'list'}), name='viajeschofer'),
	path('finalizar_viaje' , views.finaliar_viaje, name='finalizar_viaje'),
]


