from django.conf.urls import url, include
from . import views
from django.urls import path
from rest_framework import routers
from .views import BookList, AuthorList, PublisherList, StudentList, TeacherList, IssueBookTea, IssueBookStu


router = routers.DefaultRouter()
router.register(r'author', AuthorList)
router.register(r'publisher', PublisherList)
router.register(r'book', BookList)
router.register(r'student', StudentList)
router.register(r'teacher', TeacherList)

urlpatterns = [
	url(r'^teacherissue/', views.IssueBookTea.as_view()),
    url(r'^studentissue/', views.IssueBookStu.as_view()),
   
]
urlpatterns += router.urls