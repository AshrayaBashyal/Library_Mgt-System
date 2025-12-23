from django.db import models
from django.db.models import UniqueConstraint


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # published_year = models.DateField(blank=True, null=True)
    published_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    isbn = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    # returned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['book', 'member'], name='unique_book_member_borrow')
        ]
        ordering = ['-borrowed_at']      #descending order.

    def __str__(self):
        status = "returned" if self.returned else "not returned"
        return f"{self.member} borrowed {self.book} at {self.borrowed_at} and has {status}"
        #x = f"{self.member} borrowed {self.book} at {self.borrowed_at}"
        #if self.returned:
        #    return x + "and has returned"
        #else:
        #    return x + "and has not returned"