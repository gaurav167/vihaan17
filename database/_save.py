from .models import User_media, Image
from django.core.files import File

class Save:
	def input(self,u_id,data):
		User_med = User_media(user_id=u_id)
		User_med.save()
		Img = Image(user=User_med)
		Img.image = data
		Img.save()
		
	def output(self,u_id):
		out = User_media.objects.get(user_id=u_id)
		return out

