
from django.urls import path
from .views import  register, sign_in, sign_out
urlpatterns = [
    # path('accounts/', SignUpView.as_view(), name = 'signup'),
    path('register', register, name = 'register'),
    path('signin/next=/<str:next_url>',sign_in, name = 'signin'),
    path('signout',sign_out, name = 'signout'),
]