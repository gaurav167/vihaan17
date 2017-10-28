from django.shortcuts import render, get_object_or_404
from .models import User_conf, User_media, Image, Storage
from ._save import Save
from .forms import ImageUploadForm
from django.http import HttpResponse, HttpResponseForbidden

def upload(request):
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			for img in form.cleaned_data['image']:
				up = Save()
				up.input(form.cleaned_data['user_id'],img)
			return HttpResponse('image upload success')
	return HttpResponseForbidden('allowed only via POST')

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