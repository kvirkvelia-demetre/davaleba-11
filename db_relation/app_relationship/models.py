from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Passport(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )
    passport_number = models.CharField(max_length=50)

    def __str__(self):
        return self.passport_number


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees'
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(
        'Course',
        related_name='students'
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name