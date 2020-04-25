from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import users
from .models import InputFile
from .models import cars
from .serializers import UsersSerializer
from .serializers import InputFileSerializer
from .serializers import CarsSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
import os.path


# Create your views here.

@api_view(['GET', 'POST'])
def join(request):
    # 전체회원조회
    if request.method == 'GET':
        # GET통신이면 users모델전부 불러옴
        queryset = users.objects.all()
        # 불러온 모델을 json형태로 맞춰줌
        serializer = UsersSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, content_type='application/json; charset=utf-8')
    # 회원가입기능
    elif request.method == 'POST':
        # POST 통신이면 request로 들어온 JSON형태 데이터 추출
        data = JSONParser().parse(request)
        # 추출한 데이터와 우리가 선언한 serializer포맷이랑 비교 후
        serializer = UsersSerializer(data=data)
        # 같은데이터면
        if serializer.is_valid():
            # 저장
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # 다른형태면 오류 보냄
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    obj = users.objects.get(pk=pk)
    # 회원 정보 하나 가져오기
    if request.method == 'GET':
        serializer = UsersSerializer(obj)
        return JsonResponse(serializer.data, status=201)
    # 회원정보 업데이트 하기
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    # 회원 삭제하기
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@api_view(['POST'])
def login(request):
    # login 기능
    # login TEST 할 때, identify ,password 제이슨 형태로 보내야함
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_id = data['identify']
        obj = users.objects.get(identify=search_id)
        if(obj.password == data['password']):
            print(search_id)
            print(obj.password)
            return JsonResponse({"message": "login OK"}, status=200)
        return JsonResponse({"message": "login fail"}, status=400)


@api_view(['GET'])
def car(request):
    if request.method == 'GET':
        queryset = cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)


@api_view(['GET'])
def car_datail(request, num):
    obj = cars.objects.get(id=num)
    if request.method == 'GET':
        serializer = CarsSerializer(obj)
        return JsonResponse(serializer.data, status=201)


@api_view(['GET'])
def car_company_list(request, company):
    if request.method == 'GET':
        obj = cars.objects.filter(company__icontains=company)
        serializer = CarsSerializer(obj, many=True)
        print(serializer)
        return JsonResponse(serializer.data, status=201, safe=False)


@api_view(['GET'])
def car_name_list(request, name):
    if request.method == 'GET':
        obj = cars.objects.filter(name__icontains=name)
        serializer = CarsSerializer(obj, many=True)
        print(serializer)
        return JsonResponse(serializer.data, status=201, safe=False)


@api_view(['GET'])
def car_companyAll(request):
    if request.method == 'GET':
        obj = cars.objects.filter().values('company').distinct()
        print(obj)
        return HttpResponse(obj, status=201)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = InputFileSerializer(data=request.data)
        print(request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # @csrf_exempt
        # def insertdata(request):
        #    with open('./back/car_data.json', encoding='utf-8') as f:
        #        json_data = json.load(f)
        #        for i in range(len(json_data)):
        #            serializer = CarsSerializer(data=json_data[i])
        #            if serializer.is_valid():
        #                serializer.save()
        #            # return JsonResponse(serializer.errors, status=400)
        #        return JsonResponse(serializer.data, status=201)
