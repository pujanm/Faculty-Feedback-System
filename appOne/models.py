from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Subject(models.Model):
    BATCHES = tuple([("ALL", "ALL")] + [('A'+str(i),'A'+str(i)) for i in range(1,5)]+[('B'+str(i),'B'+str(i)) for i in range(1,5)])

    name = models.CharField(max_length=250, blank=False)
    semester = models.IntegerField(default=5)
    batch = models.CharField(max_length=50, choices=BATCHES, default="ALL")

    def __str__(self):
        return str(self.name) + " - Semester "  + str(self.semester)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User)
    fname = models.CharField(max_length=50, blank=False)
    lname = models.CharField(max_length=50, blank=False)
    subject = models.ManyToManyField(Subject, related_name="subject_teachers")

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)


class UserProfile(models.Model):
    BATCHES = tuple([('A'+str(i),'A'+str(i)) for i in range(1,5)]+[('B'+str(i),'B'+str(i)) for i in range(1,5)])

    user = models.OneToOneField(User)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    subject = models.ManyToManyField(Subject, related_name="subject_students")
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be of 10 digits.")
    phone_no = models.CharField(validators=[phone_regex], max_length=10)
    semester = models.IntegerField(default=3)
    batch = models.CharField(max_length=50, choices=BATCHES, default="A1")

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
