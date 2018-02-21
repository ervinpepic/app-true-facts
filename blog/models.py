import os
import random
from django.db import models

#################GlobalFunction#################

def image_name_and_path(instance, imagename):
	img_extension = os.path.splitext(imagename)
	new_image_name = random.randint(1,231321)
	final_image_name = "blog/static/images/{new_image_name}-{img_extension}".format(new_image_name=new_image_name, img_extension=img_extension)
	return final_image_name

#################END GlobalFunction#################

class Category(models.Model):
	title			= models.CharField(max_length=50)

	def __str__(self):
		return self.title

class Post(models.Model):
	title			= models.CharField(max_length=120)
	slug 			= models.SlugField(max_length=180, unique=True)
	category 		= models.ManyToManyField(Category, related_name='category')
	image			= models.ImageField(upload_to=image_name_and_path)
	body			= models.TextField()
	drafts			= models.BooleanField(default=False)
	created_date 	= models.DateTimeField(auto_now_add=True)
	edited_date		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title



