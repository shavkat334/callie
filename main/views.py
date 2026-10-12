from django.shortcuts import get_object_or_404, redirect, render
from .models import Author, Category, Post

def index(request):
    latest_posts = list(Post.objects.select_related('category', 'author').order_by('-id')[:12])
    categories = Category.objects.all()
    
    context = {
        "hot_big": latest_posts[0] if latest_posts else None,
        "hot_small": latest_posts[1:3],
        "recent": latest_posts[:6],
        "categories": categories,
        "first_cat_pk": categories.first().pk if categories.exists() else None,
    }
    return render(request, "index.html", context)

def category(request, pk=None):
    posts = Post.objects.all()
    if pk:
        cat = get_object_or_404(Category, pk=pk)
        posts = posts.filter(category=cat)
    return render(request, "category.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog-post.html", {"post": post})

def blog_post(request):
    first_cat = Category.objects.first()
    if first_cat:
        return redirect("category", pk=first_cat.pk)
    return redirect("index")

def author(request, pk=None):
    the_author = get_object_or_404(Author, pk=pk) if pk else Author.objects.first()
    posts = Post.objects.filter(author=the_author) if the_author else []
    return render(request, "author.html", {"author": the_author, "posts": posts})

def about(request):
    return render(request, "about.html")

def blank(request):
    return render(request, "blank.html")

def contact(request):
    return render(request, "contact.html")
