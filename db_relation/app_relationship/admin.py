from django.contrib import admin
from .models import Person, Passport, Employee, Department, Student, Course

admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Course)