from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=1000)
    content=models.CharField(max_length=100000)
    date=models.DateTimeField(default=timezone.now,blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title