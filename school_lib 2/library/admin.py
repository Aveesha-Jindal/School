from django.contrib import admin
from .models import Author, Publisher, Book, Teacher, Student

admin.site.register(Author)
admin.site.register(Publisher)


#register Author

class BookAuthor(admin.TabularInline):
    model = Book.author.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = (BookAuthor,)
    exclude = ('author',) # Excluding field to hide unnecessary field, as mentioned in the docs

#This is to register Student


class StudentBook(admin.TabularInline):
    model = Student.book.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentBook,)
    exclude = ('book',) # Excluding field to hide unnecessary field, as mentioned in the docs

#This is to register Teacher


class TeacherBook(admin.TabularInline):
    model = Teacher.book.through


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (TeacherBook,)
    exclude = ('book',)
    # Excluding field to hide unnecessary field, as mentioned in the docs
