# Recipe Ready Back-End

Effortlessly organize your kitchen, get instant recipes tailored to your ingredients, and cut food waste while elevating your culinary journey.

## Table of Contents

- [Overview](#overview)
  - [Try Recipe Ready](#try-recipe-ready)
- [User Guide](#user-guide)
- [Project Details](#project-details)
  - [Tech Toolkit](#tech-toolkit)
  - [Sample Code](#sample-code)
- [Front-End](#back-end)
- [Author](#author)

## Overview

Powered by Django and Django Rest Framework, Recipe Ready's backend architecture offers an array of robust features to support a seamless user experience. Leveraging Python's capabilities, the platform manages user accounts, providing secure login and registration functionalities. The application allows users to save ingredients to a personalized virtual pantry, enabling efficient organization and tracking of purchased items.

Moreover, the system facilitates the creation and management of dynamic shopping lists, ensuring a user-centric and practical approach to meal planning. Through these Django-based features, Recipe Ready ensures a user-friendly and intuitive environment, allowing individuals to curate their kitchen inventory and shopping needs with ease and precision.

### Try Recipe Ready

[Link to Recipe Ready](https://johnlombardi389.github.io/recipe-ready)

## User Guide

1. Account Creation and Login:

- Register a new account and log in to access Recipe Ready's features.
- If you prefer to jump straight in, log in with the username: test, password: test

2. Managing Pantry Ingredients:

- Add ingredients available in your kitchen to your pantry within the app.

3. Finding Recipes:

- Click the "Find Recipes" button to instantly discover recipes you can make with your current ingredients.

4. Viewing Recipes:

- Recipes display the number of missing ingredients required for preparation.

5. Accessing Recipe Details:

- Click on a recipe to view the full list of ingredients and step-by-step instructions.

6. Adding Ingredients to Shopping List:

- Each recipe includes an option to automatically add missing ingredients to your shopping list.

7. Customizing Shopping List:

- Modify your shopping list by adding any extra items you want to purchase.

8. Shopping List Management:

- From the shopping list page, delete unwanted items or mark purchased items by clicking the 'Purchased' button.

9. Automating Pantry Updates:

- Upon marking items as purchased, they will be added to your pantry automatically for future reference.

## Project Details

### Tech Toolkit

Back-End Tools:

- Python
- Django
- REST Framework
- REST API
- Git
- PythonAnywhere

Front-End Tools:

- React
- JavaScript
- Styled Components
- Sass
- CSS
- HTML
- Vite
- Git
- Figma

### Sample Code

#### Define Model

```python
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
```

Here I define a model to handle pantry ingredients owned by users. 3 different fields are set, the user who owns this ingredient, the name of the ingredient, and the purchase_date of the ingredient.

This code ensures that pantry ingredients in the Django application are associated with the user who added them, and it automatically sets the purchase date to the current date if the user hasn't specified one. The customization in the save method simplifies the process for users, providing a default value for the purchase date and making it more convenient to manage and display pantry ingredients in the application.

### Front-End

Recipe Ready is an innovative kitchen assistant app designed to streamline the culinary experience by addressing various kitchen-related challenges. With a focus on ingredient management, the application aids users in efficiently organizing their kitchen supplies, providing real-time suggestions on available recipes based on current ingredients, facilitating the creation of dynamic shopping lists, and enabling users to track the purchase dates of their ingredients.

By seamlessly integrating these features, Recipe Ready becomes an indispensable tool for users seeking to optimize their meal planning, reduce food waste, and enhance their cooking experience

- [See the Front-End Repository](https://github.com/johnlombardi389/recipe-ready)

## Author

John Lombardi

- [Portfolio](https://johnlombardi389.github.io/portfolio/)
- [LinkedIn](https://www.linkedin.com/in/johnlombardi389/)
- [GitHub](https://github.com/johnlombardi389)
