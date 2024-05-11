from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import users, SocialMediaTokens
from . serializers import usersSerializer, TokenSerializer, AnalyticsSerializer
from .authentication import authenticate
from .fetch_data import fetch_analytics_data




#authentication skipped

@api_view(['GET'])
def home(request):
    api_urls={
        'create': '/create',
        'read': '/read',
        'update': '/update',
        'delete': '/delete'
    }
    return Response(api_urls)





@api_view(['POST'])
def create(request):
    serializer=usersSerializer(data=request.data)

    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)



@api_view(['GET'])
def read(request):
    data = users.objects.all()
    serializer = usersSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def update(request, pk):
    data= users.objects.get(id=pk)
    serializer=usersSerializer(instance = data, data=request.data)

    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def delete(request, pk):
    data= users.objects.get(id=pk)
    data.delete()

    return HttpResponse('deleted')


def get_token(request, UID):
    token_data= authenticate(UID)

    if token_data:
        serializer= TokenSerializer(data=token_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Access Token Recieved")
        else:
            return HttpResponse("Error Saving Data, maybe data is not in required format.")
        
    else:
        return HttpResponse("Authentication Failed")
    


def analytics(request, UID):
    token= SocialMediaTokens.objects.get(UID=UID)
    if not token:
        return HttpResponse("Acces Token Doesn't Exist")
    else:
        analytics_data= fetch_analytics_data(token.access_token)
        if "access_token" in analytics_data:
            del analytics_data["access_token"]
        analytics_data["UID"]=UID
        serializer= AnalyticsSerializer(data=analytics_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Analytics data saved")
        else:
            return HttpResponse("Error in Fetching Data")
        # return JsonResponse(analytics_data)

