from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Project(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	subtitle = models.CharField(max_length=200)
	appname = models.CharField(max_length=200, blank=False, null=False, default="home")
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	modified_date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to='images/', default="image", blank=False)

	def publish(self):
		self.modified_date = timezone.now()
		self.save()

	def __str__(self):
		return self.subtitle

	def __str__(self):
		return self.content
