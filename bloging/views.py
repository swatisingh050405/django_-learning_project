from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User

context = {
        "posts": Post.objects.all()
    }


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'   # Default is 'object_list'
    ordering = ['-created_at']  # Order by created_at descending
    paginate_by = 3  # Number of posts per page


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'   # Default is 'object_list'
    paginate_by = 3  # Number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView( LoginRequiredMixin , CreateView):
    model = Post
    fields = ['title', 'content' , 'image']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Post
    fields = ['title', 'content' , 'image']
    template_name = 'blog/post_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 
    

    
class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'  # Redirect to home after deletion

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AllPostListView(ListView):
        model = Post
        template_name = 'blog/all_posts.html'  
        context_object_name = 'posts'
        ordering = ['-created_at']
        paginate_by = 6

def about(request):
    return render(request , 'blog/about.html')


