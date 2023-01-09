from django.db import models


class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


#  make Migration  with the command
#'python manage.py makemigrations'
def __str__(self):
    return f"title:{self.title}, description: {self.description}"
