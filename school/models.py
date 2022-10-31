
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField


class Group(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class User(AbstractUser):
    PROFESSOR = 'PROFESSOR'
    STUDENT = 'STUDENT'
    RESEARCHER = 'RESEARCHER'
    ROLE_CHOICES = [
        (PROFESSOR, 'Professor'),
        (STUDENT, 'Student'),
        (RESEARCHER, 'Researcher'),
    ]
    department = models.ForeignKey(Department,related_name='users', on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    group = models.ForeignKey(Group, related_name='users', on_delete=models.SET_NULL, null=True)


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        User, related_name='articles', on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    publish_date = models.DateField()
    journal = models.CharField(max_length=100)


class Specialization(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField()
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Course(models.Model):
    SEMESTER1 = 'S1'
    SEMESTER2 = 'S2'
    SEMESTER3 = 'S3'
    SEMESTER4 = 'S4'
    SEMESTER_CHOICES = [
        (SEMESTER1, 'Semester1'),
        (SEMESTER2, 'Semester2'),
        (SEMESTER3, 'Semester3'),
        (SEMESTER4, 'Semester4'),
    ]
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    description = models.TextField()
    semester = models.CharField(
        max_length=2, choices=SEMESTER_CHOICES, default=SEMESTER1)
    specialization = models.ForeignKey(
        Specialization, related_name='courses', on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(
        Department, related_name='courses', on_delete=models.CASCADE)
