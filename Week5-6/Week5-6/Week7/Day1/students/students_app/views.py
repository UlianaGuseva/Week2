from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import mixins


# Create your views here.

# class StudentMixinView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    
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
                 
        
class StudentListView(ListAPIView, APIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    def get_queryset(self):
        queryset = Student.objects.all()
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date_joined=date)
        else:
            queryset = Student.objects.all()
        return queryset
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
   