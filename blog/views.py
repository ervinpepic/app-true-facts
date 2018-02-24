from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#...................###..................#
from .forms import PostForm
from .models import ( 
	Post, Category, 
	get_recently_post, 
	get_last_week_post, 
	get_last_five_days_post
)
#...................###..................#

def post_list_view(request):
	post_queryset = Post.objects.all().order_by('-created_date')
	paginator = Paginator(post_queryset, 10)
	page = request.GET.get('page')
	page_post = paginator.get_page(page)
	recently_post = Post.objects.filter(created_date__gte=get_recently_post())
	category_queryset = Category.objects.all()
	template = 'blog/posts_list.html'
	context = {	
		'page_post': page_post,
		'categories': category_queryset,
		'recently_post': recently_post	
	}
	return render(request, template, context)


def post_detail_view(request, slug):
	post = get_object_or_404(Post, slug=slug)
	category = post.categories.all()
	recently_post = Post.objects.filter(created_date__gte=get_last_five_days_post())
	template = 'blog/post_detail.html'
	context = {
		'post': post,
		'related_category': category,
		'recently_post': recently_post
	}
	return render(request, template, context)

def category_detail_view(request, title):
	category = get_object_or_404(Category, title=title)
	related_category_post = category.posts.all()
	categories = Category.objects.all()
	recently_post = Post.objects.filter(created_date__gte=get_last_week_post())
	template = 'blog/category_detail.html'
	context = {
		'category': category,
		'related_category_post': related_category_post,
		'categories': categories,
		'recently_post': recently_post
	}
	return render(request, template, context)


class PostCreateView(CreateView):
	template_name = 'blog/post_form.html'
	model = Post
	form_class = PostForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super(PostCreateView, self).form_valid(form)


class PostUpdateView(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'blog/post_form.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super(PostUpdateView, self).form_valid(form)

class LoginView(FormView):
	form_class = AuthenticationForm
	success_url = reverse_lazy('blog:home')
	template_name = 'registration/login.html'

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('/blog')
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		login(self.request, form.get_user())
		return HttpResponseRedirect(self.get_success_url())


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/blog')
        return super().dispatch(*args, **kwargs)