from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="Category name", max_length=50)
    slug = models.SlugField(unique=True)
    body = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    


class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150)
    slug = models.SlugField(unique=True)
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    
       
    def __str__(self):
        return str(self.title)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"