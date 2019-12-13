# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Loan(models.Model):

	WORK_TIMES = (
		('0', 'Menos de 1 año'),
		('1', '1 año'),
        ('2', '2 años'),
        ('3', '3 años'),
        ('4', '4 años'),
        ('5', '5 años'),
        ('6', '6 años'),
        ('7', '7 años'),
        ('8', '8 años'),
        ('9', '9 años o más'),
	)

	INCOMES_RANGE = (
		('0','RD$8,000 - 15,000'),
		('1','RD$15,000 - 25,000'),
		('2','RD$25,000 - 35,000'),
		('3','RD$35,000 - 45,000'),
		('4','RD$45,000 - 55,000'),
		('5','RD$55,000 - 65,000'),
		('6','RD$65,000 - 75,000'),
		('7','RD$75,000 - 85,000'),
		('8','RD$85,000 - 95,000'),
		('9','RD$95,000 - 100,000'),
		('10','RD$95,000 - 100,000'),
		('11','RD$100,000 - 110,000'),
		('12','RD$110,000 - +'),
	)

	LOAN_REASONS = (
		('Prestamo personal','Prestamo personal'),
		('Compra vehiculo','Compra vehiculo'),
		('Compra casa','Compra casa'),
		('Vacaciones','Vacaciones'),
	)

	PROVINCES = (
		('Santo Domingo Este','Santo Domingo Este'),
		('Distrito Nacional','Distrito Nacional'),
		('Santiago','Santiago'),
		('San Cristóbal','San Cristóbal'),
		('La Vega','La Vega'),
		('Puerto Plata','Puerto Plata'),
		('San Pedro de Macorís','San Pedro de Macorís'),
		('Duarte','Duarte'),
		('La Altagracia','La Altagracia'),
		('La Romana','La Romana'),
		('San Juan','San Juan'),
		('Espaillat','Espaillat'),
		('Azua','Azua'),
		('Barahona','Barahona'),
		('Monte Plata','Monte Plata'),
		('Peravia','Peravia'),
		('Monsenor Nouel','Monseñor Nouel'),
		('Valverde','Valverde'),
		('Sanchez Ramirez','Sánchez Ramírez'),
		('Maria Trinidad Sanchez','María Trinidad Sánchez'),
		('Montecristi','Montecristi'),
		('Samana','Samaná'),
		('Bahoruco','Bahoruco'),
		('Hermanas Mirabal','Hermanas Mirabal'),
		('El Seibo','El Seibo'),
		('Hato Mayor','Hato Mayor'),
		('Dajabon','Dajabon'),
		('Elias Piña','Elias Piña'),
		('San Jose de Ocoa','San Jose de Ocoa'),
		('Santiago Rodriguez','Santiago Rodríguez'),
		('Independencia','Independencia'),
		('Pedernales','Pedernales'),
	)

	CIVIL_STATUS = (
		('0','Soltero/a'),
		('1','Casado/a'),
	)


	#Datos generales
	name = models.CharField(max_length=200, blank=False)
	personid = models.CharField(max_length=15, blank=False)
	civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS, blank=False, default=0)
	address = models.CharField(max_length=400, blank=True)
	province = models.CharField(max_length=40, choices=PROVINCES, blank=True)

	#Formas de contacto
	phone = models.CharField(max_length=15, blank=False)
	phone_home = models.CharField(max_length=15, blank=True)
	phone_office = models.CharField(max_length=15, blank=True)
	email = models.EmailField(max_length=50, blank=True)

	#Datos laborales
	work_place = models.CharField(max_length=250)
	work_time = models.CharField(max_length=1 , choices=WORK_TIMES)
	income_range = models.CharField(max_length=2, choices=INCOMES_RANGE)
	other_income = models.CharField(max_length=15, blank=True)

	#Datos prestamo
	loan_reason = models.CharField(max_length=25, choices=LOAN_REASONS)
	loan_amount = models.IntegerField()
	loan_time = models.IntegerField()
	date_req = models.DateField()

	def __str__(self):
		return self.name

class Message(models.Model):
	p_name = models.CharField(max_length=200)
	p_email = models.EmailField()
	p_phone = models.CharField(max_length=15)
	p_message = models.TextField(max_length=2000)
	message_date = models.DateField()

	def __str__(self):
		return self.p_name