# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Crypto.Cipher import AES
from Crypto import Random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms

# Create your views here.


def data_encrypt(request):
    form = forms.DataSaveForm()

    if request.method=="POST":
        form = forms.DataSaveForm(request.POST)

        if form.is_valid():
            hash_data = form.save()
            encryption_suite = AES.new("7498211973984119", AES.MODE_CBC, Random.new().read(AES.block_size))
            cipher_text = encryption_suite.encrypt(hash_data.data)
            return HttpResponseRedirect(reverse('encrypt/data_form.html'))
    return render('encrypt/data_form.html', {'form':form})
