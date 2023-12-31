"""
URL configuration for recipeready project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.login_user, name='login_user'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
    path('api/ingredients/', views.ingredients, name='ingredients-list'),
    path('api/ingredients/<int:id>/', views.ingredient_detail, name='ingredient-detail'),
    path('api/user/', views.UserInfo.as_view(), name='user-info'),
    path('api/shopping-list/', views.shopping_list_items, name='shopping-list-items'),
    path('api/shopping-list/<int:id>/', views.shopping_list_item_detail, name='shopping-list-item-detail'),
]