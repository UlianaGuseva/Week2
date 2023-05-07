from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, 
                                        IsAuthenticated, 
                                        AllowAny)
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_202_ACCEPTED)


# Create your views here.

class PostListView(APIView):
    
    permission_classes = (AllowAny, )
    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get('pk')
        
        if pk:
            try:  
                instance = Post.objects.get(id=pk)
                serializer = PostSerializer(instance)
            except Post.DoesNotExist:
                return Response({'detail': 'Post not found'}, status=HTTP_400_BAD_REQUEST)
        else: 
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return  Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                post = Post.objects.get(id=pk)
                post.delete()
                return Response({'detail': 'Post was deleted'}, status=HTTP_202_ACCEPTED)
            
            except Post.DoesNotExist:
                return Response({'detail': 'Post does not exist'}, status=HTTP_400_BAD_REQUEST )
        else:
            return Response({'detail': 'Choose one post'}, status=HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        if pk:
            try:
                post = Post.objects.get(id=pk)
                serializer = PostSerializer(post, data= request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                
            except Post.DoesNotExist:
                return Response({'detail': 'Post not found'}, status=HTTP_400_BAD_REQUEST)
            
        else:
            return Response({'detail': 'pk not found'}, status=HTTP_400_BAD_REQUEST)
            
            
    