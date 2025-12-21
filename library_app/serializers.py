# If model exists → ModelSerializer
# If no model → Serializer
# ModelSerializer → 80–90%(Automatically maps Django model → fields. Auto-implements create() / update())
# Serializer → Auth, search, analytics, dashboards(You define every field yourself. You write create() / update() manually)

from rest_framework import serializers
from .models import Book, Member, BorrowRecord

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = '__all__'