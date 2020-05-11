from django.contrib import admin
from django.apps import apps
from .models import Post, Comment
from .utils import custom_model_name

custom_models = ['post', 'comment']
app = apps.get_app_config('blogs')

class PostsAdmin(admin.ModelAdmin):
    fields = ['content', 'topic']

class CommentsAdmin(admin.ModelAdmin):
    fields = ['content', 'user', 'post']

for model_name, model in app.models.items():
    if model_name not in custom_models:
        admin.site.register(model)
    else:
        admin.site.register(model, eval(custom_model_name(model_name)))
