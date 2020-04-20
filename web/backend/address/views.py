from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Address
from .serializers import AddressSerializer

# Create your views here.


@csrf_exempt
def address_list(request):
    if request.method == 'GET':
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, content_type='application/json; charset=utf-8')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
