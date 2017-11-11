# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
def image_upload_to(instance, filename):
    return "images/%s" % filename


class Advert(models.Model):
    active = models.BooleanField(verbose_name="Отобразить", default=False)
    title = models.CharField(verbose_name="Назание", max_length=120, null=True, blank=False, unique=False)
    image = models.ImageField(null=True, help_text="Size 960x640")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title


class CategoryProduct(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=120, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    active = models.BooleanField(verbose_name="Отобразить", default=False)
    title = models.CharField(verbose_name="Назание", max_length=50, null=True)
    cover = models.ImageField(verbose_name="Обложка", null=True, help_text="Size 480x480")
    phone = models.IntegerField(verbose_name='Телефон', null=False)
    position = models.IntegerField(verbose_name='Позиция', null=False,)
    category = models.ForeignKey(CategoryProduct, verbose_name="Категория", )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name="Назание", max_length=50, null=True)
    cover = models.ImageField(verbose_name="Обложка", null=True, help_text="Size &&&")
    company = models.ForeignKey(Company, verbose_name="Компания")
    category = models.ForeignKey(CategoryProduct, verbose_name="Категория", )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)

    def __unicode__(self):
        return self.title
