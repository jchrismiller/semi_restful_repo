from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
	context={
		'users': User.objects.all()
	}
	return render(request, "login_reg/index.html", context)

def registration(request):
	result = User.objects.validate_registration(request.POST)	
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect('/')
	request.session['user_id'] = result.id
	messages.success(request, "Registration Successful!")
	return redirect('/success')

def login(request, user_id):
	result = User.objects.valudate_login(request.POST)
	if type(result) == list:
		for err in result:
			messages.error(request, err)
		return redirect('/success')

def success(request):
	try:
		request.session['user_id']
	except Keyerror:
		return redirect('/')
	context = {
		'user': User.objects.get(id=request.session['user_id'])
	}
	return render(request, 'login_reg/success.html', context)
