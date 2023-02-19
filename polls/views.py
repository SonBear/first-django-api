# Create your views here.
from django.http import HttpResponse
from .models import Student
from django.core import serializers
from django.http.response import JsonResponse

def index_students(request):
    students = Student.objects.all()
    students = map(lambda x: x.format(), list(students))
    students = list(students)
    return JsonResponse(list(students), status=200, safe=False)

def save_students(request):
    student = Student(name='Emmanuel Chable', school_id='18016328')
    student.save()
    serialized_student = serializers.serialize('json', [student])
    return JsonResponse(serialized_student, status=200, safe=False)











