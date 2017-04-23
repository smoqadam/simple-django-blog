from django.test import TestCase


# Create your tests here.
class BlogTest(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        # print(resp)
        self.assertEqual(resp.status_code, 200)

    def test_post_view(self):
        url = '/'
        resp = self.client.get(url, {'slug': 'about.html'})

        self.assertEqual(resp.status_code, 200)

    def test_category_view(self):
        resp = self.client.get('cats/', {'slug': 'python'})
        self.assertEqual(resp.status_code, 200)
