from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'age', 'level','email_id', 'phone', 'address', 'grade', 'major',)
    search_fields = ('first_name', 'student_id', 'major')
    list_filter = ('major', 'grade')
    list_per_page= 10

