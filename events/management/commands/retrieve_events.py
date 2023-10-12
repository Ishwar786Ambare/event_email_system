# notifications/management/commands/retrieve_events.py

from django.core.management.base import BaseCommand
from events.models import Event


class Command(BaseCommand):
    help = 'Retrieve event data from the Event table'

    def handle(self, *args, **options):
        events = Event.objects.all()

        with open('event_data.txt', 'w') as file:
            for event in events:
                event_info = f'Event: {event.employee.name}, Date: {event.event_date}\n'
                file.write(event_info)

        for event in events:
            self.stdout.write(self.style.SUCCESS(f'Event: {event.employee.name}, Date: {event.event_date}'))
