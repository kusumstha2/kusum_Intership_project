from rest_framework import serializers
from .models import *
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
           'student_id',
           'first_name',
           'last_name',
           'age',
           'level',
           'email_id',
           'phone',
           'address',
           'grade',
           'major',
        )
        model = Student
