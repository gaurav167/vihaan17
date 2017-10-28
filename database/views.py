from django.shortcuts import render, get_object_or_404
from .models import User_conf, User_media, Image, Storage
from ._save import Save
from django.http import HttpResponse, HttpResponseForbidden

def upload(request):
	if request.method == 'POST':
		form = request.POST
		# f = open('hi.txt',"w")
		# f.write(img)
		# f.write("\n-----\n")
		# f.close()
		up = Save()
		img = request.POST.get('img',False)
		up.input(form['user_id'],img)
		return render(request,'success.html')
	return render(request,'generic.html')

def view_image(request,_id):
	us = get_object_or_404(User_media, user_id=str(_id))
	return HttpResponse(User_media.user_id)

def home(request):
	return render(request, 'index.html',{})

def generic(request):
	return render(request, 'generic.html',{})

def elements(request):
	return render(request,'elements.html')

def signup(request):
	return render(request, 'signup.html')

def gallery(request):
	return render(request,'gallery.html') 