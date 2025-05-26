from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import database
from .serializers import UserSerializer

# CREATE
@api_view(['POST'])
def create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# READ (all)
@api_view(['GET'])
def get_all_details(request):
    all_data = database.objects.all().order_by('id')
    serializer = UserSerializer(all_data,many=True)
    return Response(serializer.data)

# EDIT,DELETE AND GET
@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, name):
    try:
        get_details = database.objects.get(name=name)
    except database.DoesNotExist:
        return Response({"error": "user not found !"}, status=404)
    
    if request.method == 'GET':
        serializer = UserSerializer(get_details)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(get_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        get_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)