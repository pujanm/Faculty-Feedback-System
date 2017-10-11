from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

def checkfor5(value):
	if value > 5 or value < 1:
		raise ValidationError('POINTS MUST BE IN THE RANGE 1 TO 5.')

# Create your models here.
class Feedback(models.Model):
	subject = models.CharField(max_length=250, default='')
	fac = models.CharField(max_length=250)
	res1 = models.IntegerField(default=True)
	res2 = models.IntegerField(default=True)
	res3 = models.IntegerField(default=True)
	res4 = models.IntegerField(default=True)
	res5 = models.IntegerField(default=True)
	res6 = models.IntegerField(default=True)
	res7 = models.IntegerField(default=True)
	res8 = models.IntegerField(default=True)
	res9 = models.IntegerField(default=True)
	sug = models.CharField(max_length=500,default='')

	
