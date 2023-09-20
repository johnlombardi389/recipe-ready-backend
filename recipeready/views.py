from .models import Ingredient
from .serializers import IngredientSerializer
from django.http import JsonResponse

def ingredients(request):
	# invoke serializer and return to client
	data = Ingredient.objects.all()
	serializer = IngredientSerializer(data, many=True)
	return JsonResponse({'ingredients': serializer.data})