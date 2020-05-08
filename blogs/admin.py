from django.contrib import admin
from .models import User, Comment, Topic, Tag, PostTag, Post

myModels = [User, Comment, Topic, Tag, PostTag, Post]

admin.site.register(myModels)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content',)
