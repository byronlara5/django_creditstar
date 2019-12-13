# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect

from loans.forms import LoanForm, MessageForm

# static pages.
def Home(request):
	return render(request, 'index.html',)

def Calculator(request):
	return render(request,'page_calculator.html',)

def Nosotros(request):
	return render(request,'nosotros.html',)

def LoanSucess(request):
	return render(request,'form_sucess.html',)




# forms.
def Contact(request):

	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			message = form.save(commit=False)
			message.message_date = timezone.now()
			form.save()
			return HttpResponseRedirect('')
	else:
		form = MessageForm()
	return render(request,'contact.html', {'form': form})

# Loan form page.
def Loan(request):

	if request.method == "POST":
		form = LoanForm(request.POST)
		if form.is_valid():
			loan = form.save(commit=False)
			loan.date_req = timezone.now()
			form.save()
			return HttpResponseRedirect('/formulario/sucess')

	else:
		form = LoanForm()
	return render(request,'form.html', {'form': form})