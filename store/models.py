from contextlib import nullcontext
from distutils.command.upload import upload
from turtle import title
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from base64 import b64encode
from django import template
register = template.Library()

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    image_bin = models.BinaryField(null=True, blank=True, default=None)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=6)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time_to_read = models.CharField(max_length=64, default='очень очень долго')
    id = models.Model.pk

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    @register.filter
    def img(self):
        return b64encode(self.image_bin).decode('utf-8')

    def get_slug(self):
        return self.slug

    def get_id(self):
        return self.id

