from django.db import models
from django.utils import timezone

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    user_name = models.CharField(max_length=50)
    pass_word = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class Post(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at  = timezone.now()

        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at  = timezone.now()

        super(Comment, self).save(*args, **kwargs)

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
