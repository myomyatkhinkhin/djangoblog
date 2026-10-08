from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post, Category
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .forms import PostForm, RegisterForm


def post_list(request,):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/post_list.html", {"page_obj": page_obj})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status="published")
    return render(request, "blog/post_detail.html", {"post": post})

def about(request):
    return render(request, "blog/about.html",{"team": "DjangoBlog Team"})

def contact(request):
    return render(request, "blog/contact.html")

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            status="published"
        ).order_by("-created_at")

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context["categories"] = Category.objects.all()
     return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(status="published")

class PostCreateView(CreateView):
    model=Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs ={"slug":self.object.slug})    


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("home")

    

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "blog/register.html"
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response