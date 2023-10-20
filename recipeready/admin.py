from django.contrib import admin
from .models import Ingredient, ShoppingListItem

admin.site.register(Ingredient)
admin.site.register(ShoppingListItem)