from django.test import TestCase
from .models import Post, Topic

class PostModelTest(TestCase):
    def setUp(self):
        topic = Topic.objects.create(name='topic')
        Post.objects.create(title='title', content='content', topic_id=topic.id)

    def test_text_context(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEqual(expected_object_name, 'title')
