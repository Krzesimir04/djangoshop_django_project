from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import Customer

@shared_task
def customer_created(customer_id):
    customer=Customer.objects.get(id=customer_id)
    subject='Zamówienie nr {}'.format(customer.id)
    message='Witaj, {}! \n\nZłożyłeś zamówienie w naszym sklepie. Identyfikator zamówienie to {}.'.format(customer.Name,customer.id)

    mail_sent=send_mail(subject,message,'admin@myshop.com',[customer.Email])

    return mail_sent