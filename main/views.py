from django.shortcuts import get_object_or_404, redirect, render
from .models import Author, Category, Post

def index(request):
    latest = list(Post.objects.all()[:12])
    first_cat = Category.objects.first() 
    
    context = {
        "hot_big": latest[0] if latest else None,
        "hot_small": latest[1:3],
        "recent": latest[:6],
        "categories": Category.objects.all(),
        "first_cat_pk": first_cat.pk if first_cat else None,
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
    if pk:
        the_author = get_object_or_404(Author, pk=pk)
    else:
        the_author = Author.objects.first()
        
    posts = Post.objects.filter(author=the_author) if the_author else []
    return render(request, "author.html", {"author": the_author, "posts": posts})

def about(request):
    return render(request, "about.html")

def blank(request):
    return render(request, "blank.html")

def contact(request):
    return render(request, "contact.html")
