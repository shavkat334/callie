from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index_2"),
    path("about/", views.about, name="about"),
    path("author/", views.author, name="author"),
    path("author/<int:pk>/", views.author, name="author_detail"),
    path("blank/", views.blank, name="blank"),
    path("post/", views.blog_post, name="blog_post"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("category/", views.category, name="category"),
    path("category/<int:pk>/", views.category, name="category_detail"),
    path("contact/", views.contact, name="contact"),
]
