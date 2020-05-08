from django.db import models
from django.utils import timezone

class User(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dis_name = models.CharField(max_length=50, verbose_name='display name')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(User, self).save(*args, **kwargs)

class Topic(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    content = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Post, self).save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, through='PostTag')

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()

        return super(Comment, self).save(*args, **kwargs)

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
