from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password1 = 'password'
        self.password2 = 'password'

    def test_signup_page_url(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')
        self.assertTemplateUsed(response, template_name='base12md.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')
        self.assertTemplateUsed(response, template_name='base12md.html')

    def test_registration(self):
            self.client.post('signup', {
                'username': 'test1',
                'email': 'email@email.com',
                'password1': '12345',
                'password2': '12345'
            })

            user = User.objects.create(username='test1', password='12345')
            user.save()

            self.assertTrue(User.objects.filter(username='test1').exists())


class LoginPageTests(TestCase):

    def setUp(self) -> None:
        self.username = 'testuser'
        self.password1 = '12345'

    def test_login_page_url(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/login.html')
        self.assertTemplateUsed(response, template_name='base12md.html')

    def test_login_page_view_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/login.html')
        self.assertTemplateUsed(response, template_name='base12md.html')

    def test_login_page_view(self):
        user = User.objects.create(username='testuser', email='test_user1@test.com')
        user.set_password('12345')
        user.save()
        self.user = user

        client = Client()
        client.force_login(self.user)
        response = client.post(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)




