from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)  # 图片上传

    def __str__(self):
        return self.title

    def update_content(self, new_content):
        self.content = new_content
        self.updated_at = timezone.now()
        self.save()

    def delete_post(self):
        self.delete()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return f'Comment by {self.author.username}'

    def update_content(self, new_content):
        self.content = new_content
        self.updated_at = timezone.now()
        self.save()

    def delete_comment(self):
        self.delete()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

# Create your models here.
