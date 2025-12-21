from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.DateField()

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        #x = f"{self.member} borrowed {self.book} at {self.borrowed_at}"
        #if self.returned:
        #    return x + "and has returned"
        #else:
        #    return x + "and has not returned"
        status = "returned" if self.returned else "not returned"
        return f"{self.member} borrowed {self.book} at {self.borrowed_at} and has {status}"