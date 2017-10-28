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
        form = request.POST
        hash_data = form['data']
        u_id = form['user_id']
        u = User_conf(user_id=u_id)
        u.save()
        #save hash and image meta
        f = Fernet(b'W4mdwJuyFWo67WzrPu3Z0l79uTu95UVI5yEbstkLmw4=')
        encryption_suite = f.encrypt(str.encode(hash_data))
        m = hashlib.md5()
        m.update(encryption_suite)
        return render(request, 'success.html')
    return render(request, 'sub_data.html')


def retrieve(request):
    return render(request,'ret_data.html')
