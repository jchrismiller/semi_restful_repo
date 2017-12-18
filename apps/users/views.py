from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect


def index(request):
	context = {
		'users': User.objects.all()
	}
	return render(request, "users/index.html", context)

def new(request):
	return render(request, "users/create.html")

def create(request):
	User.objects.create(
		first_name = request.POST['first_name'], 
		last_name = request.POST['last_name'], 
		email = request.POST['email']
	)
	return redirect('/users')

def edit(request, user_id):
	context = {
		'user': User.objects.get(id=user_id)
	}
	return render(request, 'users/update.html', context)

def update(request, user_id):

	user_to_update = User.objects.get(id=user_id)
	user_to_update.first_name = request.POST['first_name']
	user_to_update.last_name = request.POST['last_name']
	user_to_update.email = request.POST['email']
	user_to_update.save()
	return redirect('/users')

def show(request, user_id):
	context = {
		'user': User.objects.get(id=user_id)
	}
	return render(request, 'users/show.html', context)

def destroy(request, user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/users')
