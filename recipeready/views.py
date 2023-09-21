from .models import Ingredient
from .serializers import IngredientSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'DELETE'])
def ingredients(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                ingredient = Ingredient.objects.get(pk=id)
                serializer = IngredientSerializer(ingredient)
                return Response(serializer.data)
            except Ingredient.DoesNotExist:
                return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
             data = Ingredient.objects.all()
             serializer = IngredientSerializer(data, many=True)
             return Response({'ingredients': serializer.data})
        
    elif request.method == 'DELETE':
        try:
            ingredient = Ingredient.objects.get(pk=id)
            ingredient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)