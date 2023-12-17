
from django.shortcuts import render
from .models import Content
from django.db.models import Count

def content_list(request):
    genres = Content.GENRE_CHOICES  # Assuming GENRE_CHOICES is defined in the Film model
    contents = Content.objects.all()
    genres= Content.objects.values('genre').annotate(total_content=Count('genre'))

    # Filter out genres with zero content
    genres_with_content = [entry['genre'] for entry in genres if entry['total_content'] > 0]

    context = {
        'title': 'Content shop',
        'active_links': 'content',
        'genres': genres_with_content,
        'contents': contents,
    }

    return render(request, 'content_shop/content_list.html', context)

def content_detail(request, slug, id):
    content = Content.objects.get(id=id)
    context = {
        'content':content,
        'title': content.title,
        'active_links': 'content',
    
    }

    return render(request, 'content_shop/content_detail.html', context)