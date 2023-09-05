from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ["-date_created"]

    def __str__(self):
        return self.title
