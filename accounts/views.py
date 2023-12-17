
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from books.models import Book


# class SignUpView(generic.CreateView):
#     form_class    = UserCreationForm
#     success_url   = reverse_lazy('login')
#     template_name = 'signup.html'


def register(request):
    error_msg = ''
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        # username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        try:
          # Create the user
          user = User.objects.create_user(username=email, email=email, password=password) 
          return redirect('login')  # Redirect to the login page after successful registration
        except Exception:
            error_msg = 'Email already used!'
    context = {
        'title': 'Register',
        'active_links': 'user' ,
        'error_msg':error_msg,
     }
     
    return render(request, 'accounts/register.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def sign_in(request, next_url):
    error_msg = ''
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            if next_url == 'home':
               return redirect('home')  # Redirect to the home page after successful login
            else:
              #when user tries to buy without signin, redirect the user to signin and back to the buy page after signin
              try:
                book = Book.objects.get(id=next_url)
                return redirect(f'/books/details/{book.slugify}/{book.id}')
              except Exception:
                print('Book not found')
            
        else:
            # Authentication failed, show an error message
            error_msg = "Invalid username or password!"
    
    context = {
        'title': 'Sign In',
        'active_links': 'user' ,
        'error_msg':error_msg,
    }

    return render(request, 'accounts/login.html', context)


def sign_out(request):
    if request.user.is_authenticated:
       logout(request)
    return redirect('home') 