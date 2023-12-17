
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('about', about_view, name = 'about'),
    path('contact', contact_view, name = 'contact'),
]