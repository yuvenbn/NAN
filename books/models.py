
from django.db import models
from django.urls import reverse
import re
from django.contrib.auth.models import User

class BookCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
       return self.name

class Book(models.Model):
    category = models.ForeignKey(BookCategory, null=True, on_delete=models.CASCADE)
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    isbn = models.CharField(null=True, max_length = 200)
    pub_date = models.DateField(null=True)
    price = models.FloatField(null=True, blank=True)
    premium_price = models.FloatField(null=True, blank=True, default=0)
    tag = models.CharField(max_length = 200, null=True)
    description = models.CharField(max_length = 500, default=None)
  
    image_url = models.CharField(max_length = 2083, default=False)
    follow_author = models.CharField(max_length=2083, blank=True)  
    book_available = models.BooleanField(default=False)
    book_featured = models.BooleanField(default=False) #featured books appear on home page

    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    pdf_document = models.FileField(upload_to='pdf_documents/', null=True)

    def __str__(self):
        return self.title
    
    def slugify(self):
        """
        Method to return the name of the book slugified
        """
        # Convert to lowercase and replace spaces with hyphens
        result = self.title.lower().replace(" ", "-")
        
        # Remove any characters that are not alphanumeric or hyphen
        result = re.sub(r"[^a-z0-9-]", "", result)
        
        # Remove consecutive hyphens
        result = re.sub(r"-+", "-", result)
        
        # Remove leading and trailing hyphens
        result = result.strip("-")
        return result


class Order(models.Model):
    product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    download_token = models.CharField(max_length=255, null=True)
    created =  models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.product.title
