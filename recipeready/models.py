from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    purchase_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the purchase_date to the current date if it hasn't been set by the user
        if not self.purchase_date:
            self.purchase_date = timezone.now().date()
        super().save(*args, **kwargs)
 
    def __str__(self):
        return self.name
    
class ShoppingListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_list')
    item = models.CharField(max_length=100)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     saved_recipes_data = models.JSONField(blank=True, null=True)

#     def __str__(self):
#         return self.user.username