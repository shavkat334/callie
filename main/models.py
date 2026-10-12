from django.db import models


class Category(models.Model):
    name = models.CharField("Nomi", max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField("Ismi", max_length=100)
    bio = models.TextField("Haqida", blank=True)
    avatar = models.ImageField("Rasm", upload_to="avatars/", blank=True)

    class Meta:
        verbose_name = "Muallif"
        verbose_name_plural = "Mualliflar"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Sarlavha", max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="posts"
    )
    image = models.ImageField("Rasm", upload_to="posts/", blank=True)
    summary = models.TextField("Qisqacha mazmun", blank=True)
    content = models.TextField("Matn")
    created_at = models.DateTimeField("Sana", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField("Ismi", max_length=100)
    email = models.EmailField("Email")
    text = models.TextField("Izoh")
    created_at = models.DateTimeField("Sana", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"

    def __str__(self):
        return f"{self.name}: {self.post}"
