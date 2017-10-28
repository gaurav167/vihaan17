from django.contrib import admin
from .models import User_media, User_conf, Image, Storage

# Register your models here.

admin.site.register(User_conf),
admin.site.register(User_media),
admin.site.register(Image),
admin.site.register(Storage)