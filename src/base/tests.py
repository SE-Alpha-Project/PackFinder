from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_user_signup(self):
        """Test user registration"""
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@ncsu.edu',
            'password1': 'complex_password123',
            'password2': 'complex_password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        """Test user login"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_user_logout(self):
        """Test user logout"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

class ProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_profile_creation(self):
        """Test profile is created automatically"""
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_profile_update(self):
        """Test profile update"""
        response = self.client.post(reverse('profile'), {
            'bio': 'Test bio content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Profile.objects.get(user=self.user).bio, 'Test bio content')

class MessagingTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user('user1', password='pass123')
        self.user2 = User.objects.create_user('user2', password='pass123')
        self.client.login(username='user1', password='pass123')

    def test_inbox_view(self):
        """Test inbox page loads"""
        response = self.client.get(reverse('messages'))
        self.assertEqual(response.status_code, 200)

    def test_send_message(self):
        """Test sending a message"""
        response = self.client.post(reverse('send_message', args=[self.user2.id]), {
            'content': 'Test message content'
        })
        self.assertEqual(response.status_code, 302)

class ViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='testpass123')

    def test_welcome_page(self):
        """Test welcome page loads"""
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)

    def test_find_people_page(self):
        """Test find people page loads"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('find-people'))
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_access(self):
        """Test unauthorized access redirects to login"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

class FormValidationTests(TestCase):
    def test_invalid_signup(self):
        """Test signup with invalid data"""
        response = self.client.post(reverse('signup'), {
            'username': 'user',
            'email': 'invalid-email',
            'password1': 'pass123',
            'password2': 'different123'
        })
        self.assertEqual(response.status_code, 200)  # Stay on same page with errors
        self.assertFalse(User.objects.filter(username='user').exists())

    def test_invalid_login(self):
        """Test login with wrong credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'nonexistent',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)

class SecurityTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='testpass123')

    def test_password_change(self):
        """Test password change functionality"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('password_change'), {
            'old_password': 'testpass123',
            'new_password1': 'newpass123',
            'new_password2': 'newpass123'
        })
        self.assertEqual(response.status_code, 302)

    def test_csrf_protection(self):
        """Test CSRF protection"""
        self.client.handler.enforce_csrf_checks = True
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 403)  # CSRF check failed

class UITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

    def test_navbar_presence(self):
        """Test navbar appears when logged in"""
        response = self.client.get(reverse('welcome'))
        self.assertContains(response, 'navbar')

    def test_profile_picture_upload(self):
        """Test profile picture upload"""
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        response = self.client.post(reverse('profile'), {
            'profile_picture': image
        })
        self.assertEqual(response.status_code, 302)

    def test_responsive_design(self):
        """Test mobile viewport meta tag"""
        response = self.client.get(reverse('welcome'))
        self.assertContains(response, 'viewport')

class CompatibilityQuizTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

    def test_quiz_submission(self):
        """Test quiz submission"""
        response = self.client.post(reverse('compatibility_quiz'), {
            'question_1': 'answer1',
            'question_2': 'answer2'
        })
        self.assertEqual(response.status_code, 302)

    def test_quiz_results(self):
        """Test quiz results page"""
        response = self.client.get(reverse('quiz_results'))
        self.assertEqual(response.status_code, 200) 