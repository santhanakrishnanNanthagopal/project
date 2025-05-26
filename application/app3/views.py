from rest_framework import viewsets,filters

from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .models import Student, Course, Subscription
from .serializers import StudentSerializer, CourseSerializer, SubscriptionSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    @action(detail=False, url_path=r'(?P<name>[^/.]+)', methods=['get'])
    def get_by_name(self, request, name=None):
        subscription = Subscription.objects.filter(student__name__icontains=name).first()
        if subscription:
            data = {
                "id": subscription.id,
                "name": subscription.student.name,
                "age": subscription.student.age,
                "Degree": subscription.student.Degree,
                "Course": subscription.course.Course,
                "duration": subscription.course.duration
            }
            return Response(data)
        return Response({"message": "No subscription found."}, status=status.HTTP_404_NOT_FOUND)