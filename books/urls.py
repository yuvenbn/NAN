
from django.urls import path
from .views import( BooksListView, 
                    BooksDetailView, 
                    BookCheckoutView, 
                    paymentComplete, 
                    SearchResultsListView, 

                    books_list,
                    book_detail, 
                    download_book,
                    book_search,
                    )

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', books_list, name = 'books'),
    path('list', BooksListView.as_view(), name = 'list'),
    
    path('<int:pk>/', BooksDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', BookCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
    
    path('search', book_search, name = 'book-search'),
    path('details/<str:slug>/<int:id>', book_detail, name = 'details'),
    path('<str:download_token>/download/', download_book, name='download_book'),
    
    

]