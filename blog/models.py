import os
import random


from django.urls import reverse
from django.db import models
from django.conf import settings

#################GlobalFunction#################

def image_name_and_path(instance, imagename):
	img_extension = os.path.splitext(imagename)
	new_image_name = random.randint(1,231321)
	final_image_name = "blog/{new_image_name}-{img_extension}".format(new_image_name=new_image_name, img_extension=img_extension)
	return final_image_name

#################END GlobalFunction#################

class Post(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vlasnik_postova', on_delete=models.CASCADE, default=1)
	title			= models.CharField(max_length=120)
	slug 			= models.SlugField(max_length=180, unique=True)
	categories 		= models.ManyToManyField('Category', related_name='posts')
	image			= models.ImageField(upload_to=image_name_and_path)
	body			= models.TextField()
	drafts			= models.BooleanField(default=False)
	created_date 	= models.DateTimeField(auto_now_add=True)
	edited_date		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'slug': self.slug})

	# def recently_post(self):
	# 	now = timezone.now()
	# 	return now - datetime.timedelta(days=2) <= self.created_date <= now



class Category(models.Model):
	title			= models.CharField(max_length=50)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:category_detail', kwargs={'title': self.title})