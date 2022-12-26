from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )

    def test_string_representation(self):
        newpost = Post(title='A sample title')
        self.assertEqual(str(newpost), newpost.title)

    def test_post_content(self):
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        res = self.client.get(reverse('home'))

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Nice body content')
        self.assertTemplateUsed(res, 'home.html')

    # def test_post_detail_view(self):
    #     res = self.client.get('/post/1/')
    #     print('res:', res)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertContains(res, 'A good title')
    #     self.assertTemplateUsed(res, 'post_detail.html')
