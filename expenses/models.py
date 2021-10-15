from django.db import models


class Expense(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    amount = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.amount}"
