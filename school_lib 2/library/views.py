from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from .models import Author, Publisher, Book, Teacher, Student
from .serializers import BookSerializer, PublisherSerializer, AuthorSerializer, StudentSerializer, TeacherSerializer
from rest_framework import viewsets


class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorList(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherList(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherList(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class IssueBookTea(APIView):

    def get(self, request):

        teacherid = request.GET.get('studentid', False)
        bookid = request.GET.get('bookid', False)
        teacher = Teacher.objects.filter(pk=studentid).last()
        book = Book.objects.get(pk=bookid)
        print(teacher.book_count)

        if teacher.book_count == 4:
            return Response("You have already issued 4 books")

        elif book.issued is True:
            return Response("The requested book is currently unavailable")

        elif teacher.book_count != 4 and book.issued is False:
            teacher.book_count += 1
            teacher.book.add(bookid)
            book.issued = True
            teacher.save()
            book.save()
            return Response ("Book Issued Successfully and your due date is "+ str(teacher.due_date))
        
        else:
            return Response("Error")



class IssueBookStu(APIView):

    def get(self, request):
        studentid = request.GET.get('studentid', False)
        bookid = request.GET.get('bookid', False)
        student = Student.objects.filter(pk=studentid).last()
        book = Book.objects.get(pk=bookid)

        if student.book_count == 2:
            return Response("You have already issued 2 books")

        elif book.issued is True:
            return Response("The requested book is currently unavailable")

        elif student.book_count != 2 and book.issued is False:
            student.book_count += 1
            student.book.add(bookid)
            book.issued = True
            student.save()
            book.save()
            return Response ("Book Issued Successfully and your due date is "+ str(student.due_date))
        
        else:
            return Response("Error")


