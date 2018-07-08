from rest_framework import serializers
from .models import Author, Publisher, Book, Teacher, Student


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'category', 'author', 'publisher']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'book', 'issue_date', 'due_date']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name', 'book', 'issue_date', 'due_date']
