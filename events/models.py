from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()


class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=100)
    template_content = models.TextField()
    subject = models.CharField(max_length=500)


class EmailLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    error_message = models.TextField()


class ExecutionLog(models.Model):
    last_execution_time = models.DateTimeField()
