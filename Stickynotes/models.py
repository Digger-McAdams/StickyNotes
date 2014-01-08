from django.db import models
from django.contrib.auth.models import User
# Create your models herea
class Entry(models.Model):
	message=models.CharField(max_length=40)
	created=models.DateTimeField(auto_now_add=True)
	date=models.DateField(blank=True)
	completed=models.BooleanField(default=False)
	priority_choices=(
		(1,'Low'),
		(2,'Medium'),
		(3,'High'),
	)
	priority=models.IntegerField(choices=priority_choices,default=1)
