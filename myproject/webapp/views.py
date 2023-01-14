from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer

class employeeList(APIView):
    def get(self, request):
        employee1=employee.objects.all()
        serializers=employeeSerializer(employee1, many=True)
        return Response(serializers.data)

    def post(self):
        pass



