# content_shop/models.py
from django.db import models
import re

class Content(models.Model):
    GENRE_CHOICES = [
        ('Released Films', 'Released Films'),
        ('Sitcoms', 'Sitcoms'),
        ('TV Drama Series', 'TV Drama Series'),
        ('Epic Drama Series', 'Epic Drama Series'),
        ('TV Talk Shows', 'TV Talk Shows'),
        ('Reality Shows', 'Reality Shows'),
        ('Documentary', 'Documentary'),
        ('Comedy', 'Comedy'),
    ]

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='film_thumbnails/')

    def __str__(self):
        return self.title

    def slugify(self):
        """
        Method to return the title of the content slugified
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
