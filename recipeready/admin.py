from django.contrib import admin
from .models import Ingredient, ShoppingListItem, UserProfile

admin.site.register(Ingredient)
admin.site.register(ShoppingListItem)
admin.site.register(UserProfile)