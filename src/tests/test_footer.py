from django.test import TestCase, Client
from django.urls import reverse


class FooterTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Assuming you have a page that includes the footer
        self.response = self.client.get(reverse('home'))  # Adjust 'home' to your actual URL name
        
    def test_footer_social_links_exist(self):
        """Test that all social media links are present in the footer"""
        social_links = [
            'https://www.facebook.com/PackFinder',
            'https://twitter.com/PackFinder',
            'https://www.instagram.com/PackFinder',
            'https://www.linkedin.com/company/PackFinder'
        ]
        
        for link in social_links:
            self.assertContains(self.response, link)
            
    def test_footer_copyright_text(self):
        """Test that the copyright text is present and correct"""
        copyright_text = "© 2024 PackFinder. All rights reserved."
        self.assertContains(self.response, copyright_text)
        
    def test_footer_social_icons(self):
        """Test that all social media icons are present"""
        social_icons = [
            'fa-facebook-f',
            'fa-twitter',
            'fa-instagram',
            'fa-linkedin-in'
        ]
        
        for icon in social_icons:
            self.assertContains(self.response, icon)
            
    def test_footer_styling_classes(self):
        """Test that essential styling classes are present"""
        required_classes = [
            'bg-blue-900',
            'text-white',
            'max-w-screen-xl',
            'mx-auto',
            'text-center'
        ]
        
        for css_class in required_classes:
            self.assertContains(self.response, css_class)