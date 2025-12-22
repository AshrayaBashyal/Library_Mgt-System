from rest_framework import generics
from .models import Book, Member, BorrowRecord
from .serializers import BookSerializer, MemberSerializer, BorrowRecordSerializer
# Create your views here.

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberRetrieveUpdateDestroyVIew(generics.RetrieveUpdateDestroyAPIView)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowRecordListCreateView(generics.ListCreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

class BorrowRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer