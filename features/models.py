from django.db import models
from django.contrib.auth.models import User


class Feature(models.Model):

    name = models.CharField(max_length=100)
    details = models.TextField()

    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    Done = 'Done'
    Doing = 'Doing'
    ToDo = 'ToDo'
    PHASE_OF_DEVELOPMENT_CHOICES = [
        (Done, 'Done'),
        (Doing, 'Doing'),
        (ToDo, 'ToDo'),
        ]
    phase_of_development = models.CharField(max_length=6,
                                            choices=PHASE_OF_DEVELOPMENT_CHOICES,
                                            default='ToDo')
    upvote = models.IntegerField(default=0)
    vote_price = models.DecimalField(max_digits=4,
                                     decimal_places=2, default=10.00)

    def __str__(self):
        return self.name