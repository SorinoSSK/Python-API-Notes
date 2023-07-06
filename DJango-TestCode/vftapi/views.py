import json
import requests

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import StreamingHttpResponse

from channels.layers import get_channel_layer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import asyncio

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from crate import client

url = 'https://vflowtech-test.aks1.eastus2.azure.cratedb.net:4200'
ID = 'admin'
PWD = 'g3A5)GEhA8ZFiC$M$4(&h_Wk'
headers = {
    'Accept': 'text/event-stream'
}


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

async def getCrateDBCluster(request):
    conn = client.connect(url, username=ID, password=PWD, verify_ssl_cert=True)

    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sys.cluster")
        result = cursor.fetchone()
    return JsonResponse({"Crate DB Cluster": result})

def stream_sse_events(connQuery):
    print(len(connQuery))
    if (connQuery != None):
        for row in connQuery:
            # print(row);
            yield 'data: {}\n\n'.format(row)
    yield 'data: completed'

async def streamSSESKTests(request):
    conn = client.connect(url, username=ID, password=PWD, verify_ssl_cert=True)
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT person_id, person_name, person_description FROM sktest LIMIT 100;")
        response = StreamingHttpResponse(stream_sse_events(cursor.fetchall()), content_type='text/plain')
        return response
    
def onSteamingComplete(channelLayer):
    async_to_sync(channelLayer.group_send)(
        'EndOfLine',
        {
            'type': 'message',
            'content': 'completed'
        }
    )

# async def getUnit9Data(request): #, pageSize, pageNumber, toDate, fromDate
#     pageSize = int(request.GET.get('page_size'))
#     pageNumber = int(request.GET.get('page_number'))
#     toDate = request.GET.get('to_date')
#     fromDate = request.GET.get('from_date')
#     offset = pageSize*(pageNumber-1)
#     conn = client.connect(url, username=ID, password=PWD, verify_ssl_cert=True)
#     with conn:
#         cursor = conn.cursor()
#         query = "SELECT data FROM unitdata9 WHERE timestamp >= " + str(fromDate) + " AND " + str(toDate) + " LIMIT " + str(pageSize) + " offset " + str(offset) + ";"
#         cursor.execute(query)
#         response = StreamingHttpResponse(stream_sse_events(cursor.fetchall()), content_type='text/event-stream')
#         return response


async def getUnit9Data(request): #, pageSize, pageNumber, toDate, fromDate
    pageSize = int(request.GET.get('page_size'))
    pageNumber = int(request.GET.get('page_number'))
    toDate = request.GET.get('to_date')
    fromDate = request.GET.get('from_date')
    offset = pageSize*(pageNumber-1)

    response = HttpResponse(content_type='text/event-stream')
    response['Connection'] = 'keep-alive'
    response['Cache-Control'] = 'no-cache'
    response['x-Accel Buffering'] = 'no'

    conn = client.connect(url, username=ID, password=PWD, verify_ssl_cert=True)
    
    chunk_size = 4096
    with conn:
        cursor = conn.cursor()
        query = "SELECT data FROM unitdata9 WHERE timestamp >= " + str(fromDate) + " AND " + str(toDate) + " LIMIT " + str(pageSize) + " offset " + str(offset) + ";"
        cursor.execute(query)
        data = cursor.fetchall()


        return response