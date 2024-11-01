from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings
from base.forms import CustomUserCreationForm
from base.tokens import account_activation_token

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        subject = 'Activate Your FindMyRoomie Account'
        message = render_to_string('registration/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            'protocol': 'https' if self.request.is_secure() else 'http'
        })

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,  # Use the Gmail address
                recipient_list=[user.email],
                fail_silently=False,
            )
            print(f"Email sent successfully to {user.email}")
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            user.delete()
            form.add_error(None, "Failed to send activation email. Please try again.")
            return self.form_invalid(form)

        return response 