from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

    
class Bug(models.Model):

    DOING = 'Doing'
    DONE = 'Done'
    STATUS_CHOICES = ((DONE, 'Done'),
                      (DOING, 'Doing'),)
    title = models.CharField(max_length=100, blank=False)

    details = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='Doing')
    posted_on = models.DateTimeField(
                                     null=True,
                                     blank=True,
                                     default=timezone.now
                                    )
    comment = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    bug = models.ForeignKey(
                            Bug,
                            on_delete=models.CASCADE,
                            related_name='comment'
                            )
    created_on = models.DateTimeField(
                                      null=True,
                                      blank=True,
                                      default=timezone.now
                                    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment