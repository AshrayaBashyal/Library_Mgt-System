from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),

    path('members/', MemberListCreateView.as_view()),
    path('members/<int:pk>/', MemberRetrieveUpdateDestroyView.as_view()),

    path('borrows/', BorrowRecordListCreateView.as_view()),
    path('borrows/<int:pk>/', BorrowRecordRetrieveUpdateDestroyView.as_view()),
]
