from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = ('first_name',)
    search_fields = ('first_name',)