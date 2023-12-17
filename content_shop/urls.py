
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list', content_list , name = 'content_list'),
    path('<str:slug>/<int:id>/details', content_detail , name = 'content_detail'),
]