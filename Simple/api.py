from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource

from Simple.models import Advert, Product, Company, CategoryProduct


class AdvertResource(ModelResource):
    class Meta:
        limit = 0

        queryset = Advert.objects.all()
        resource_name = 'advert'


class CategoryResource(ModelResource):
    class Meta:
        limit = 0

        queryset = CategoryProduct.objects.all()
        resource_name = 'category'


class CompanyResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', null=True)

    class Meta:
        limit = 0

        queryset = Company.objects.all()
        resource_name = 'company'


class ProductResource(ModelResource):
    company = fields.ForeignKey(CompanyResource, 'company', null=True)
    category = fields.ForeignKey(CategoryResource, 'category', null=True)

    class Meta:
        limit = 4

        queryset = Product.objects.all()
        resource_name = 'product'
        filtering = {
            'title': ALL_WITH_RELATIONS,
            'company': ALL_WITH_RELATIONS,
            'category': ALL_WITH_RELATIONS,
        }

        class_paginator = Paginator
