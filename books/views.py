from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Book, BookCategory , Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json
import uuid
import random
from django.http import FileResponse
from django.shortcuts import get_object_or_404

def download_book(request, download_token):
	try:
		order = Order.objects.get(download_token=download_token, user=request.user)
		book = order.product
		# # Assuming the book has a 'pdf' field that stores the PDF file
		if book.pdf_document:
			file_path = book.pdf_document.path
			file_name = book.pdf_document.name.split('/')[-1]  # Extract the file name from the file path

			response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
			return response

	except Exception:
         return redirect('error_page')


def book_detail(request, slug, id):
	book = Book.objects.get(id=id) 
	context = {
		'book': book,
		'random_books': Book.objects.order_by('?')[:4],
		'title':book.title,
		"active_links" : 'books',
	}
	return render(request, 'books/book-detail.html', context)

class BooksListView(ListView):
    model = Book
    template_name = 'list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)

	book = Book.objects.get(id=body['productId'])
	user = request.user
	download_token = str(uuid.uuid4())
	Order.objects.create(
		product=book,
		user=user,
		download_token=download_token
	)

	download_link = f'/books/{download_token}/download'
	data = {
		'message':'Payment Completed',
		'download_link':download_link,
	}

	return JsonResponse(data, safe=False)



def book_search(request):
	print('starting') 
	query = request.GET.get('q')
	if query:
		# Perform the search query using case-insensitive matching
		books = Book.objects.filter(
			Q(title__icontains=query) |
			Q(description__icontains=query) |
			Q(author__icontains=query)
		)
	else:
		books = Book.objects.none()  # Return an empty queryset if no query is provided

	context = {
		'query': query,
		'books': books,
		'title': 'Search results',
		'active_links': 'books',
		
	}

	return render(request, 'books/search-results.html', context)

def books_list(request):
    categories_with_books = BookCategory.objects.filter(book__isnull=False).distinct()
    context = {'categories': categories_with_books}
    return render(request, 'books/books_list.html', context)