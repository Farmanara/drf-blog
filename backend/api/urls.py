from django.urls import path,include
from .views import ArticleViewSet

app_name='api'

urlpatterns=[

    path('',ArticleViewSet.as_view({'get':'list'}),name='list'),
    path('<int:pk>',ArticleViewSet.as_view({'get':'retrieve'}),name='detail')

]