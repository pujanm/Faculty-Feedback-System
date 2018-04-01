from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    sap_id = models.BigIntegerField(blank=False, unique=True)

    def __str__(self):
        return str(self.sap_id)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User)
    fname = models.CharField(max_length=50, blank=False)
    lname = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)


class Feedback(models.Model):
    user = models.ForeignKey("auth.User")
    subject = models.CharField(max_length=250, default='AOA')
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')
    res1 = models.IntegerField(default=1)
    res2 = models.IntegerField(default=1)
    res3 = models.IntegerField(default=1)
    res4 = models.IntegerField(default=1)
    res5 = models.IntegerField(default=1)
    res6 = models.IntegerField(default=1)
    res7 = models.IntegerField(default=1)
    res8 = models.IntegerField(default=1)
    res9 = models.IntegerField(default=1)
    sug = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.subject
