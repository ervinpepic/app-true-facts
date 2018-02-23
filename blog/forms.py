from django import forms
from .models import Post, Category

# Create the form class.
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title", 
			"slug", 
			"categories", 
			"image", 
			"body", 
			"drafts"
		]
