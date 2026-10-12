from django.shortcuts import get_object_or_404, redirect, render
from .models import Author, Category, Post

def index(request):
    latest = list(Post.objects.select_related('category', 'author').order_by('-id')[:12])
    cats = Category.objects.all()
    return render(request, "index.html", {
        "hot_big": latest[0] if latest else None,
        "hot_small": latest[1:3],
        "recent": latest[:6],
        "categories": cats,
        "first_cat_pk": cats.first().pk if cats.exists() else None,
    })

def category(request, pk=None):
    posts = Post.objects.filter(category__pk=pk) if pk else Post.objects.all()
    return render(request, "category.html", {"posts": posts})

def post_detail(request, slug):
    return render(request, "blog-post.html", {"post": get_object_or_404(Post, slug=slug)})

def blog_post(request):
    first = Category.objects.first()
    return redirect("category", pk=first.pk) if first else redirect("index")

def author(request, pk=None):
    author = get_object_or_404(Author, pk=pk) if pk else Author.objects.first()
    return render(request, "author.html", {"author": author, "posts": Post.objects.filter(author=author) if author else []})

def about(request): return render(request, "about.html")
def blank(request): return render(request, "blank.html")
def contact(request): return render(request, "contact.html")
