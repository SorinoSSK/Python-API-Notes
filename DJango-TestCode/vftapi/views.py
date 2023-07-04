from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

# from .serializers import TestAPISerializer
# from .models import testApi
# Create your views here.

# class testAPIViewSet(viewsets.ViewSet):
#     queryset = testApi.objects.all()
#     serializer_class = TestAPISerializer
# class testAPIViewSet(viewsets.ModelViewSet):
#     queryset = testApi.objects.all()
#     serializer_class = TestAPISerializer

#     @action(detail=True, methods=['get'])
#     def get(self, request):
#         return Response({"Success":"API is online"})

async def testAPIViewSet(request):
    return JsonResponse({"Success": "API is online"})