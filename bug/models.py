from django.db import models
from django.contrib.auth.models import User


class Bug(models.Model):

    Done = 'Done'
    Doing = 'Doing'
    ToDo = 'ToDo'
    FIX_STATUS_CHOICES = [
        (Done, 'Done'),
        (Doing, 'Doing'),
        (ToDo, 'ToDo'),
        ]

    title = models.CharField(max_length=100)
    details = models.TextField()
    fix_status = models.CharField(
                                  max_length=6,
                                  choices=FIX_STATUS_CHOICES,
                                  default='ToDo'
                                )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    bug = models.ForeignKey(
                            Bug,
                            on_delete=models.CASCADE,
                            related_name='comments'
                            )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment