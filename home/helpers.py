from django.utils.text import slugify

from .models import BlogModel
import string
import random


def generate_random_string(N):
    res="".join(random.choices(string.ascii_uppercase+string.digits,k=N))

    return res

def generate_slug(text):
    from .models import BlogModel
    new_slug=slugify(text)

    if BlogModel.objects.filter(slug=new_slug).exists():
        return generate_slug(text+ generate_random_string(5))
    return new_slug
from django.conf import settings
from django.core.mail import send_mail

def send_mail_to_user(token,email):
    subject=f"Verification email to log into travel diaries "
    message=f"Hi paste the link to verify account http://127.0.0.1/verify/{token}"
    email_from =settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
