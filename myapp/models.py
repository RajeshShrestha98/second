from django.db import models

class Content(models.Model):
    heading = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='image')
    button_link = models.URLField()
    button_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title  # ✅ FIXED