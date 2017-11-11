# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Simple.models import Advert, Company, CategoryProduct, Product


class AdvertAdmin(admin.ModelAdmin):
    list_display = ['title', ]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductOfCompanyAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Advert, AdvertAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CategoryProduct, CategoryAdmin)
admin.site.register(Product, ProductOfCompanyAdmin)
