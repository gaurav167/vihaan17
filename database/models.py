from django.db import models

class User_media(models.Model):
	user_id = models.CharField(max_length=30)

	def __str__(self):
		return user_id

class User_conf(models.Model):
	user_id = models.CharField(max_length=30)
	def __str__(self):
		return user_id

class Image(models.Model):
	user = models.ForeignKey(User_media, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='static/img/pic_folder',height_field=None,width_field=None,default='static/img/default.jpg')
	def __str__(self):
		return user

class Storage(models.Model):
	img_id = models.ForeignKey(Image, on_delete=models.CASCADE)
	pixel_no = models.BigIntegerField()
	user = models.ForeignKey(User_conf, on_delete=models.CASCADE)
	_hash = models.CharField(max_length=20)
	def __str__(self):
		return user