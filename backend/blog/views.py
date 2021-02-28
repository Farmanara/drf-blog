# from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView , DetailView
from .models import Article

class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.all()


class ArticleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(Article,pk=self.kwargs.get('pk'))