from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    purchase_date = models.DateField(default=timezone.now)
    # user_id = models.IntegerField

    def save(self, *args, **kwargs):
        # Update the purchase_date to the current date if it hasn't been set by the user
        if not self.purchase_date:
            self.purchase_date = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name