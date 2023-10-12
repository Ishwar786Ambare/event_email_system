from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event, EmailTemplate, Employee, EmailLog
from django.core.mail import send_mail
from datetime import date


class SendEmailView(APIView):
    def post(self, request):
        # 1. Retrieve event data
        events = Event.objects.filter(event_date=date.today())

        for event in events:
            # 2. Fetch email template
            email_template = EmailTemplate.objects.get(event_type=event.event_type)

            # 3. Populate email template
            subject = email_template.subject
            body = email_template.body.format(employee_name=event.employee.name, event_date=event.event_date)

            from_email = 'your_email@gmail.com'

            # 4. Send email
            try:
                self.send_email_with_retry(event, subject, body, from_email, [event.employee.email])
                EmailLog.objects.create(event=event, status='Sent successfully')
            except Exception as e:
                self.handle_email_error(event, e)

            # 5. Log email sending status and errors (you can implement this part)
        return Response({"message": "Emails sent successfully."}, status=status.HTTP_200_OK)

    def send_email_with_retry(self, event, subject, body, from_email, recipient, max_attempts=3):
        attempts = 0
        while attempts < max_attempts:
            try:
                send_mail(subject, body, from_email, recipient)
                return
            except Exception as e:
                attempts += 1
                self.handle_email_error(event, e)
        # If the email has failed after all retry attempts, mark it as failed
        EmailLog.objects.create(event=event, status='Failed to send after retries')

    def handle_email_error(self, event, error):
        # Log the error and additional information as needed
        EmailLog.objects.create(event=event, status=f'Error sending email to {event.employee.name}: {str(error)}')