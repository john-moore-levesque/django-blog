from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from taggit.managers import TaggableManager
from django.utils.crypto import get_random_string
from django import forms
from meta.models import ModelMeta


# Create your models here.
class PostCategory(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'post category'
        verbose_name_plural = 'post categories'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(ModelMeta, models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField(default="Summary")
    body = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = TaggableManager(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    _metadata = {
        'title': 'title',
        'image': 'get_meta_image',
        'description': 'abstract',
    }

    def get_meta_image(self):
        if self.image:
            return self.image.url

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.author, self.slug])
