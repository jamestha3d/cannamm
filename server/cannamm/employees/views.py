from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls = {
        'List':'/employees/',
        'Detail view':'/details/ <str:pk>/',
        'Create':'/add/',
        'Update':'/update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def employeeList(request):
    employees = Employee.objects.all()
    cities = City.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employeeDetail(request, pk):
    employee = Employee.objects.get(id=pk)
    cities = City.objects.all()
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def employeeUpdate(request, pk):
    employee = Employee.objects.get(id=pk)
    #edit here
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def employeeDelete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    #edit here
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Deleted Successfully')