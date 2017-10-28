from .models import User_media, Image
from django.core.files import File
class Save:
	user_id = '0'
	def input(self,u_id,data):
		User_media = User_media(user_id=u_id)
		User_media.save()
		Image = Image(user=User_media)
		Image.image = data
		Image.save()
		
	def output(self,u_id):
		out = User_media.objects.get(user_id=u_id)
		return out

