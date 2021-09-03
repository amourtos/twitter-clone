from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TwitterUser(AbstractUser):
    # following = models.ManyToManyField('TwitterUser', related_name='following')
    # followers = models.ManyToManyField('TwitterUser', related_name='followers')

    def __str__(self):
        return self.username


class Tweet(models.Model):
    body = models.CharField(max_length=140)
    time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        TwitterUser,
        related_name="created_by",
        on_delete=models.CASCADE
    )
    like = models.ForeignKey(
        TwitterUser,
        related_name="like",
        on_delete=models.CASCADE
    )


class Notification(models.Model):
    pass
