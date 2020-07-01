from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body", "category"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "body", "category"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else:
            return False


def add_comment_to_post(request, author, slug):
    form = CommentForm()
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_detail', author=post.author, slug=post.slug)
        else:
            form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


def blog_categories(request, slug):
    category = Post.category.values_list('id', flat=True).filter(slug=slug)
    posts = Post.objects.filter(category__in=category)
    return render(request, 'blog_category.html', {"category": slug, "posts": posts})


def blog_index(request, author):
    posts = Post.objects.filter(author__in=author)
    return render(request, 'blog_index.html', {"author": author, "posts": posts})


def blog_detail(request, author, slug):
    author = Post.author.get_queryset().filter(username=author).values_list('id', flat=True)
    post = Post.objects.filter(author__in=author).get(slug=slug)
    return render(request, 'blog_detail.html', {"author": author, "post": post})


def blog_home(request, slug=None, author=None):
    context = {}
    category = slug
    if category:
        category_id = Post.category.filter(slug=category).values_list('id', flat=True)
    else:
        category_id = None

    if author:
        author_id = Post.author.get_queryset().filter(username=author).values_list('id', flat=True)
    else:
        author_id = None

    if not category_id and not author_id:
        posts = Post.objects.all()
        context = {"posts": posts}
    elif category_id and not author_id:
        posts = Post.objects.filter(category__in=category_id)
        context = {"category": category, "posts": posts}
    elif author_id and not category_id:
        posts = Post.objects.filter(author__in=author_id)
        context = {"author": author, "posts": posts}
    else:
        posts = Post.objects.filter(author__in=author_id, category__in=category_id)
        context = {"category": category, "posts": posts, "author": author}
    return render(request, 'blog_category.html', context)
