from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    isDone = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


