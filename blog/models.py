import datetime
import os
from django.db import models
from django.urls import reverse
import random
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.text import slugify


#################GlobalFunction#################

def image_name_and_path(instance, imagename):
	img_extension = os.path.splitext(imagename)
	new_image_name = random.randint(1,231321)
	final_image_name = "blog/{new_image_name}-{img_extension}".format(new_image_name=new_image_name, img_extension=img_extension)
	return final_image_name

def get_recently_post():
	today = datetime.date.today()
	yesterday = today - datetime.timedelta(1)
	return yesterday

def get_last_week_post():
	today = datetime.date.today()
	last_week_post = today - datetime.timedelta(7)
	return last_week_post

def get_last_five_days_post():
	today = datetime.date.today()
	last_week_post = today - datetime.timedelta(5)
	return last_week_post
#################END GlobalFunction#################

class Post(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vlasnik_postova', on_delete=models.CASCADE, default=1)
	title			= models.CharField(max_length=120)
	slug 			= models.SlugField(max_length=180, unique=True, blank=True)
	categories 		= models.ManyToManyField('Category', related_name='posts')
	image			= models.ImageField(upload_to=image_name_and_path)
	body			= RichTextField()
	drafts			= models.BooleanField(default=False)
	created_date 	= models.DateTimeField(auto_now_add=True)
	edited_date		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


class Category(models.Model):
	title			= models.CharField(max_length=50)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:category_detail', kwargs={'title': self.title})