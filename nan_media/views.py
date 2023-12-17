from django.shortcuts import render

# Create your views here.
from books.models import Book, BookCategory
from django.core.mail import send_mail

import smtplib
import ssl


 

def create_categories():
        book_categories = [
        'Fiction',
        'Non-Fiction',
        'Children\'s Books',
        'Poetry',
        'Plays and Scripts',
        'Graphic Novels/Comics',
        'Reference Books',
        'Religious/Spiritual',
        'Art and Photography',
        'Science and Technology',
        'Romance'
        ]
        #Creating book categories
        for category in book_categories:
                if not BookCategory.objects.filter(name=category):
                        BookCategory.objects.create(name=category)

def home(request):
    active_links = ["home"]
    title = 'Home'
    books = Book.objects.order_by('-id')[:8] #Querying the 8 most recently added books
    #Create default book categories
    create_categories()
    
    context ={ 
            'active_links': active_links,
            'books': books,
            'title':title,
    }
    return render(request, 'nan_media/home.html', context) 

def contact_view(request):
    context = {
            'active_links':'contact',
            'title':'Contact us',
    }    
    if request.method == 'POST':
        # send_email()
        name = request.POST.get('name')
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        receiver_email = 'contact@nanmediapublisher.com'
        
        send_mail(
            'NAN Media Message',
            f'Name: {name}\nEmail: {sender_email}\nSubject: {subject}\nMessage: {message}',
            sender_email,
            [receiver_email],
            fail_silently=False,
        )
        return render(request, 'nan_media/email_success.html', context)
    
    return render(request, 'nan_media/contact.html', context)


def about_view(request):
    context = {
            'active_links':'about',
            'title':'About us',
    }    
    return render(request, 'nan_media/about.html', context)

# def send_email():
#     # SMTP server settings
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#     sender_email = 'yuvenb5@gmail.com'
#     receiver_email = 'yuvenb5@gmail.com'
#     password = 'jqoixmvqbxmvqinf'
    
#     # Email content
#     subject = 'Test Email'
#     body = 'This is a test email.'
#     message = f'Subject: {subject}\n\n{body}'
    
#     # Create an SSL context
#     context = ssl.create_default_context()
    
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls(context=context)
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)