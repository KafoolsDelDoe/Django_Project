from django.contrib import admin

# Register your models here.

from .models import admin

from .models import Student, Portfolio

admin.site.register(Student)
admin.site.register(Portfolio)
