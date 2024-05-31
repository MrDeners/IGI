import pytest
from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/main_page.html')
        self.assertIsNotNone(response.context['news'])


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/signup.html')


class SignInViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signin_view(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/signin.html')


@pytest.mark.django_db
class TestIndexView:
    def test_index_view(self, client, news_factory):
        news_factory.create()
        response = client.get(reverse('index'))
        assert response.status_code == 200
        assert 'news' in response.context


@pytest.mark.django_db
class TestSignUpView:
    def test_signup_view(self, client, user_factory):
        user_factory.create(username='testuser', password='testpassword')
        response = client.post(reverse('signup'), data={
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        assert response.status_code == 302
        assert response.url == reverse('home')


@pytest.mark.django_db
class TestSignInView:
    def test_signin_view(self, client, user_factory):
        user_factory.create(username='testuser', password='testpassword')
        client.login(username='testuser', password='testpassword')
        response = client.get(reverse('signin'))
        assert response.status_code == 302
        assert response.url == reverse('home')


@pytest.mark.django_db
class TestAboutView:
    def test_about_view(self, client, about_factory):
        about_factory.create()
        response = client.get(reverse('about'))
        assert response.status_code == 200
        assert 'about' in response.context


@pytest.mark.django_db
class TestDoctorPageView:
    def test_doctor_page_view(self, client, doctor_factory):
        doctor = doctor_factory.create()
        response = client.get(reverse('doctor_page', kwargs={'pk': doctor.pk}))
        assert response.status_code == 200
        assert 'doctor' in response.context


@pytest.mark.django_db
class TestClientPageView:
    def test_client_page_view(self, client, client_factory, doctor_factory):
        client = client_factory.create()
        doctor = doctor_factory.create(client=client)
        client.doctorCard = doctor
        client.save()
        client.refresh_from_db()
        response = client.get(reverse('client_page'))
        assert response.status_code == 200
        assert 'doctor' in response.context


@pytest.mark.django_db
class TestApiRequestsView:
    def test_api_requests_view(self, client):
        response = client.get(reverse('api_requests'))
        assert response.status_code == 200
        assert 'cat_fact' in response.context
        assert 'dog_image' in response.context
