from django.contrib import admin
from .models import Profile, Product, Comment, Rating, Cart, CartItem, Payment, ProductHistory

admin.site.register([Profile, Product, Comment, Rating, Cart, CartItem, Payment, ProductHistory])
