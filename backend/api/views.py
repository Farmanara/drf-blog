# from django.shortcuts import render

# Create your views here.

from blog.models import Article
from .serializers import ArticleSerializer
# from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView
from rest_framework import viewsets,serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404





class ArticleViewSet(viewsets.ViewSet):
    def list(self,request): 
        queryset=Article.objects.all()
        serializer=ArticleSerializer(queryset,many=True)
        return Response(serializer.data)


    def retrieve(self,request,pk=None):
        queryset=Article.objects.all()
        article=get_object_or_404(queryset,pk=pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)

# class ArticleList(ListCreateAPIView):
#     queryset=Article.objects.all()
#     serializer_class= ArticleSerializer

# class ArticleDetail(RetrieveUpdateAPIView):
#     queryset=Article.objects.all()
#     serializer_class= ArticleSerializer


