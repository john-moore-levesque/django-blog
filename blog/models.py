from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from taggit.managers import TaggableManager
from django.utils.crypto import get_random_string
from django import forms


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


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = TaggableManager(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.author, self.slug])


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[post.get_absolute_url(), self.slug])

    def save(self, *args, **kwargs):
        self.slug = get_random_string(32)
        try:
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)
