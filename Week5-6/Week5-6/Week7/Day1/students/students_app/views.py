from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from rest_framework.status import HTTP_204

# Create your views here.

class StudentList(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class StudentDetail(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance)
        return Response(serializer.data)
    
    
    def put(self, request, *args, **kwargs):
        pk =  kwargs.get('pk')

        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'detail': 'Student was deleted'})
                 
        
            