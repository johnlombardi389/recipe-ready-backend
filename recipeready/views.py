from .models import Ingredient
from .serializers import IngredientSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsIngredientOwner


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
@permission_classes([IsAuthenticated, IsIngredientOwner])
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
def login_user(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        authenticated_user = authenticate(request=request, username=username, password=password)

        if authenticated_user is not None:
            # Generate authentication tokens
            refresh = RefreshToken.for_user(authenticated_user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access': access_token,
                'refresh': refresh_token,
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # Check if a user with the provided username already exists
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            return Response({'error': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create(username=username, password=make_password(password), email=email)

        # Generate authentication tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'access': access_token,
            'refresh': refresh_token,
        }, status=status.HTTP_201_CREATED)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)