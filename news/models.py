from django.db import models
import re

# Create your models here.
class NewsArticle(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        publication_date = models.DateField(auto_now_add=True)
        image = models.ImageField(upload_to='news_images/', null=True, blank=True)

        def __str__(self):
            return self.title

        def slugify(self):
       
            # Convert to lowercase and replace spaces with hyphens
            result = self.title.lower().replace(" ", "-")
            
            # Remove any characters that are not alphanumeric or hyphen
            result = re.sub(r"[^a-z0-9-]", "", result)
            
            # Remove consecutive hyphens
            result = re.sub(r"-+", "-", result)
            
            # Remove leading and trailing hyphens
            result = result.strip("-")
            return result

