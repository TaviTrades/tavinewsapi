from django.urls import path
from .views import NewsAPIView, NewsDetail

urlpatterns = [
    path('news/', NewsAPIView.as_view(), name='news'),
    path('news/<str:uuid>/', NewsDetail.as_view(), name='news_detail'),
]
