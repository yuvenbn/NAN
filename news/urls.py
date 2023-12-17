
from django.urls import path
from .views import news_list, news_details
urlpatterns = [
    path('articles', news_list, name = 'news_articles'),
    path('<str:slug>/<int:id>/details', news_details, name = 'news_article_details'),
   
]