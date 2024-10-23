from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # For storing the commenter's name
    body = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'