from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Degree = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Course(models.Model):
    Course = models.CharField(max_length=100)
    duration = models.IntegerField()
    venu=Student.objects.all()
    def __str__(self):
        return self.Course

class Subscription(models.Model):   
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    