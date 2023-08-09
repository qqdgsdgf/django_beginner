from django.test import TestCase
from django.urls import reverse  # new
from posts.models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text='This is a test!')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'This is a test!')

    def test_url_exists_at_correct_location(self):  # new
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  # new
        response = self.client.get(reverse('posts.home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/posts/home.html')
        self.assertContains(response, 'This is a test!')
