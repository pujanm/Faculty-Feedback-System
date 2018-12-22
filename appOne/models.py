from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return str(self.name)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User)
    fname = models.CharField(max_length=50, blank=False)
    lname = models.CharField(max_length=50, blank=False)
    subject = models.ManyToManyField(Subject, related_name="subject_teachers")

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    subject = models.ManyToManyField(Subject, related_name="subject_students")

    def __str__(self):
        return str(self.user.username)


class Feedback(models.Model):
    student = models.ForeignKey(UserProfile)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherProfile)
    res1 = models.IntegerField(default=1)
    res2 = models.IntegerField(default=1)
    res3 = models.IntegerField(default=1)
    res4 = models.IntegerField(default=1)
    res5 = models.IntegerField(default=1)
    res6 = models.IntegerField(default=1)
    res7 = models.IntegerField(default=1)
    res8 = models.IntegerField(default=1)
    res9 = models.IntegerField(default=1)
    sug = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.student.user.username + " - " + self.subject.name
