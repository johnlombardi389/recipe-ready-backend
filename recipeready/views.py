from .models import Ingredient
from .serializers import IngredientSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ingredients(request, id=None):
    if request.method == 'GET':
        ingredients = Ingredient.objects.filter(user=request.user)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response({'ingredients': serializer.data})
        
    elif request.method == 'POST':
        # Create an ingredient for the authenticated user
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associate the ingredient with the authenticated user
            return Response({'ingredient': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ingredient_detail(request, id):
    try:
        ingredient = Ingredient.objects.get(pk=id)
    except Ingredient.DoesNotExist:
        return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the ingredient belongs to the authenticated user
    if ingredient.user != request.user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            ingredient = Ingredient.objects.get(pk=id)
            ingredient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        password = data.get('password')
        data['password'] = make_password(password)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User registered and logged in successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)