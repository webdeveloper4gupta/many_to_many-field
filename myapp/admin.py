from django.contrib import admin
from myapp.models import Student,Course,Streams

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Streams)
