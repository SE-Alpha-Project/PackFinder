from django.core.mail import send_mail
from django.conf import settings

# Example usage in a view
send_mail(
    subject='Your Subject',
    message='Your Message',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=['recipient@example.com'],
    fail_silently=False,
) 