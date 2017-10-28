# -*- coding: utf-8 -*-
# from Crypto.Cipher import AES
# from Crypto import Random
import hashlib
from cryptography.fernet import Fernet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DataSaveForm
from database.models import User_conf, Storage

# Create your views here.


def data_encrypt(request):
    if request.method=="POST":
        form = forms.DataSaveForm(request.POST)
        if form.is_valid():
            hash_data = form.cleaned_data['data']
            u_id = form.cleaned_data['user_id']
            u = User_conf(user_id=u_id)
            u.save()
            #save hash and image meta
            f = Fernet(b'W4mdwJuyFWo67WzrPu3Z0l79uTu95UVI5yEbstkLmw4=')
            encryption_suite = f.encrypt(hash_data.data)
            m = hashlib.md5()
            m.update(encryption_suite)


            return HttpResponseRedirect(reverse('success.html'))
    return render(request, 'sub_data.html')

# def data_decrypt(request):


def retrieve(request):
    return render(request,'ret_data.html')
