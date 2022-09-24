from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Title(models.Model):
	'''用户记录的标题'''
	text = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True)

	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		'''返回模型的字符串表示'''
		return self.text
		
class Write(models.Model):
	'''用户记录的内容'''
	title = models.ForeignKey(Title, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		'''返回模型的字符串表示'''
		return f'{self.text[:50]}...'
