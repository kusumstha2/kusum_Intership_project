from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'age', 'email_id', 'phone', 'address','level', 'grade', 'major',]

