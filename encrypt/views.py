# -*- coding: utf-8 -*-
# from Crypto.Cipher import AES
# from Crypto import Random
import hashlib
from cryptography.fernet import Fernet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DataSaveForm
from database.models import User_conf, Storage, Image

import cv2
import matplotlib.pyplot as plt
from pylab import*
import numpy as np


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
        l = 10
        start = 0
        while start < len(encryption_suite):
            ur = Image.objects.filter(is_used=0)
            ur.is_used = 1
            ur = list(ur)[0]
            url = os.path.join(r"C:\Users\Gaurav\Desktop\web-d\projects\hackathons\vihaan17\venv\backend\static\img\pic_folder", )
            end = start + l - 1
            if end > len(encryption_suite):
                end = len(encryption_suite) - 1
            i,j = blobdetector(url)
            k = i
            matrix = encode(url,encryption_suite[start:end+1],i,j)
            ss = Storage(img_id = ur.id,i=i,j=j,k=k,user=u.id,_hash=m)
        return render(request, 'success.html')
    return render(request, 'sub_data.html')


def retrieve(request):
    if request.method == POST:
        form = request.POST
        u_id = form['user_id']
        user = User_conf.objects.get(user_id=u_id)
        msg = decode(matrix,k,j,80)
        converbgrtorgb(matrix)
        image = Image.objects.latest()
        return redner(request,'gallery.html',{'image':image})
    return render(request,'ret_data.html')


def encode(path,data,i,j):
    
    img = cv2.imread(path)
    #dimension = list(img.shape)
    count = 0
    
    #Here we input the mesage 
    encrypted_message = data
    
    bitstr = ''.join('{0:08b}'.format(ord(i),'b') for i in encrypted_message)
    
    length = len(bitstr)
    while(count < length):
        #img[i,100] = update(img[i,100])
        rgb = img[i,j]
        k = 0
        for k in range(3):
            bit = list('{0:08b}'.format(rgb[k]))
            bit[-1] = bitstr[count]
            count = count + 1
            newbit = "".join(bit)
            rgb[k] = int(newbit,2)
            if(count == length):
                break
        
        if(count == length):
            break
        i+=1
        
        
    return img


    
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


def decode(img,i1,j,size):
    #img = cv2.imread(path)
    getbitstr = ""
    decrypt = ""
    for i in range(size):
        for k in img[i1,j]:
            bit = list('{0:08b}'.format(k))
            getbitstr = getbitstr + str(bit[7])
        i1+=1
        decrypt = decode_binary_string(getbitstr) 
    return(decrypt [:size//8])


    
#second arguement is an encrypted sliced data
def blobdetector(path):
        
    im = cv2.imread(path)
    
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    
    # Change thresholds
    params.minThreshold = 0
    params.maxThreshold = 150
    
    
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 200
    
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.01
    
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.8
    
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    
    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)
    
    
    # Detect blobs.
    keypoints = detector.detect(im)
    
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob
    
    diameter = []
    for i in keypoints:
        diameter.append(i.size)
        
    d = max(diameter)
    ind = diameter.index(d)
    
    x = keypoints[ind].pt[0]
    x = int(x)
    y =  keypoints[ind].pt[1]
    y = int(y)
    
    return x,y



def converbgrtorgb(matrix):
    m = matrix.shape
    for i in range(m[0]):
        for j in range(m[1]):
            l = matrix[i,j]
            r = []
            r.append(l[2])
            r.append(l[1])
            r.append(l[0])
            matrix[i,j] = r