from django.test import TestCase, Client


# Create your tests here.
class URLTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_getting_the_link(self):
        response = self.c.post('/generate_code/', {'url': 'https://contest.yandex.ru/contest/14977/enter/'})
        self.assertEqual(response.status_code, 200)

    def test_link_dublicate(self):
        response = self.c.post('/generate_code/', {'url': 'https://contest.yandex.ru/contest/14977/enter/'})
        responseSecond = response = self.c.post('/generate_code/', {'url': 'https://contest.yandex.ru/contest/14977/enter/'})
        self.assertEqual(response.content, responseSecond.content)

    def test_redirect(self):
        response = self.c.post('/generate_code/', {'url': 'https://example.com'})
        redirect = (response.content[21:]).decode("utf-8")
        print(redirect)
        response = self.c.get(redirect)
        self.assertEqual(response.status_code, 200)