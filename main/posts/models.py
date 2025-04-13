# posts/models.py
from django.db import models
from user.models import User

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    caption = models.TextField()  # fixed typo from "captions" to "caption"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)  # Added this field
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"