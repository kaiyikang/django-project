from sre_parse import expand_template
from rest_framework import serializers
from .models import Image, Product, Category, Company, ProductSite, ProductSize, Comment
from rest_flex_fields import FlexFieldsModelSerializer
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes = 'product_headshot'
    )
    
    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']



class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk','name','url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields =['pk','name']
        expandable_fields = {
            'products': ('reviews.ProductSerializer',{'many':True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk','name']



class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk','name','price','url','created','updated']
        expandable_fields = {
            'product' : 'reviews.CategorySerializer',
            'productsize':'reviews.ProductSizeSerializer',
            'company': 'reviews.CompanySerializer',
        }


class ProductSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Product
        fields = ['pk','name','created','content', 'updated']
        expandable_fields = {
            'category' : ('reviews.CategorySerializer', {'many':True}),
            'sites':     ('reviews.ProductSiteSerializer',{'many':True}),
            'comments':  ('reviews.CommentSerializer',{'many':True}),
            'image': ('reviews.ImageSerializer', {'many':True}),
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk','title','content','created','updated']
        expandable_fields = {
            'prodcut': 'reviews.CategorySerializer',
            'user':'reviews.UserSerializer'
        }