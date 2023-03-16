from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_verification_mail(user, code):
    subject = 'Verify your email address'
    template_name = 'Email_verification.html'
    context = {'user': user , "code":code}
    html_message = render_to_string(template_name, context)
    text_message = ' '
    from_email = "israaessmat172@outlook.com"
    to_email = [user.email]
    email = EmailMultiAlternatives(subject,text_message, from_email, to_email , )
    email.attach_alternative(html_message, 'text/html', )
    email.send(fail_silently=False)

def send_passwordreset_verification_mail(user, code):
    subject = 'reset password request'
    template_name = 'password_reset_verification.html'
    context = {'user':user , "code":code}
    html_message = render_to_string(template_name, context)
    text_message = 'reset password request'
    from_email = "israaessmat172@outlook.com"
    to_email = [user.email]
    email = EmailMultiAlternatives(subject,text_message, from_email, to_email , )
    email.attach_alternative(html_message, 'text/html', )
    email.send(fail_silently=False)

