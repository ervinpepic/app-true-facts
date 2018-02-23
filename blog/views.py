from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#...................###..................#
from .models import Post, Category
from .forms import PostForm
#...................###..................#
# Create your views here.

def post_list_view(request):
	template = 'blog/posts_list.html'
	category_queryset = Category.objects.all()
	recently_post = Post.objects.filter(created_date__gte=datetime.date.today())
	print(recently_post)
	post_queryset = Post.objects.all().order_by('-created_date')
	paginator = Paginator(post_queryset, 10)
	page = request.GET.get('page')
	page_post = paginator.get_page(page)
	context = {	
		'page_post': page_post,
		'categories': category_queryset		
	}
	return render(request, template, context)

def post_detail_view(request, slug):
	post = get_object_or_404(Post, slug=slug)
	category = post.categories.all()
	template = 'blog/post_detail.html'
	context = {
		'post': post,
		'related_category': category,	
	}
	return render(request, template, context)

def post_create_view(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404	
	create_form = PostForm(request.POST or None, request.FILES or None)
	if create_form.is_valid():
		post_form = create_form.save(commit=False)
		post_form.user = request.user
		post_form.save()
		messages.success(request, "Successfully created post. Thank you.")
		return HttpResponseRedirect('/blog')
	context = {
		"form": create_form,
	}
	return render(request, "blog/post_form.html", context)

def category_detail_view(request, title):
	category = get_object_or_404(Category, title=title)
	related_category_post = category.posts.all()
	template = 'blog/category_detail.html'
	context = {
		'category': category,
		'related_category_post': related_category_post
	}
	return render(request, template, context)


