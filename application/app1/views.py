from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def create(request):
    serializer=Student(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.error,status=404)

@api_view(['GET'])
def get_all_details(request):
    data=Student.objects().all(order_by='name')
    serializer=StudentSerializer(data,many=True)
    return Response(serializer.data,status=200)
@api_view(['GET'])
def get_particular_data(requset,pk):
    data=Student.objects.get(pk=pk)
    except Student.DoesNotExist():
    