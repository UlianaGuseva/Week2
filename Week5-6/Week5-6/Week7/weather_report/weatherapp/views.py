from django.shortcuts import render

# Create your views here.
from .models import Report
from .serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_400_BAD_REQUEST, 
                                   HTTP_202_ACCEPTED)




class ReportView(APIView):
    
    def get(self, request, *args, **kwargs):
        
    
        pk = kwargs.get('pk')
        
        if pk:
            try:  
                instance = Report.objects.get(id=pk)
                serializer = ReportSerializer(instance)
            except Report.DoesNotExist:
                return Response({'detail': 'Post not found'}, status=HTTP_400_BAD_REQUEST)
        else: 
            queryset = Report.objects.all()
            serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return  Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                report = Report.objects.get(id=pk)
                report.delete()
                return Response({'detail': 'Report was deleted'}, status=HTTP_202_ACCEPTED)
            
            except Report.DoesNotExist:
                return Response({'detail': 'Report does not exist'}, status=HTTP_400_BAD_REQUEST )
        else:
            return Response({'detail': 'Choose one report'}, status=HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        if pk:
            try:
                report = Report.objects.get(id=pk)
                serializer = ReportSerializer(report, data= request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                
            except Report.DoesNotExist:
                return Response({'detail': 'Report not found'}, status=HTTP_400_BAD_REQUEST)
            
        else:
            return Response({'detail': 'pk not found'}, status=HTTP_400_BAD_REQUEST)
            
            
    
    
    