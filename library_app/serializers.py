# If model exists → ModelSerializer
# If no model → Serializer
# ModelSerializer → 80–90%(Automatically maps Django model → fields. Auto-implements create() / update())
# Serializer → Auth, search, analytics, dashboards(You define every field yourself. You write create() / update() manually)

from rest_framework import serializers
from .models import Book, Member, BorrowRecord
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    def validate_published_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError('The published year cannot be in the future!')
        return value

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

# next: nested serializers?