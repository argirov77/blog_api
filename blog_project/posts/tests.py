from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


# Create your tests here.
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):

            testuser1 = User.objects.create_user(username='testuser1', password='abc123')
            testuser1.save()

            testpost1 = Post.objects.create(author=testuser1, title='blog title', body=f'content body')
            testpost1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'blog title')
        self.assertEqual(body, 'content body')
