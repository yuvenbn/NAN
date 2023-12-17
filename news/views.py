from django.shortcuts import render
from .models import NewsArticle

def news_list(request):
    # Retrieve a list of news articles ordered by creation date
    news_articles = NewsArticle.objects.order_by('-publication_date')
    context = {
        'title':'News',
        'active_links':'news',
        'news_articles': news_articles

    }

    return render(request, 'news/news_list.html', context)

def news_details(request, slug, id):
    # Retrieve a list of news articles ordered by creation date
    news_article = NewsArticle.objects.get(id=id)
    context = {
        'title':news_article.title ,
        'active_links':'news',
        'news_article': news_article,

    }
    return render(request, 'news/news_details.html',context)
