from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

from users.models import CustomUser



class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return str(self.title)+"-"+str(self.author)




class LeaveApplication(models.Model):
    APPROVE_CHOICE1 = (
        ('SICK LEAVE', 'SICK LEAVE'),
        ('PERSONAL LEAVE', 'PERSONAL LEAVE'),
        ('SABBATICAL LEAVE', 'SABBATICAL LEAVE'),
        ('MATERNITY LEAVE', 'MATERNITY LEAVE'),
    )

    APPROVE_CHOICE = (
        ('APPROVAL PENDING', 'APPROVAL PENDING'),
        ('APPROVED', 'APPROVED'),
        ('NOT APPROVED', 'NOT APPROVED'),
    )
    reasons = models.CharField(blank=True, max_length=100, choices=APPROVE_CHOICE1)

    subject = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)

    approval = models.CharField(blank=True, max_length=100, choices=APPROVE_CHOICE,default='APPROVAL PENDING')
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)


class Announcement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author)

class ExpenseApplication(models.Model):
    subject = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    file=models.FileField()
    APPROVE_CHOICE = (
        ('APPROVAL PENDING','APPROVAL PENDING'),
        ('APPROVED', 'APPROVED'),
        ('NOT APPROVED', 'NOT APPROVED'),
    )
    approval = models.CharField(blank=True,default='APPROVAL PENDING' ,max_length=100, choices=APPROVE_CHOICE)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount = models.CharField(blank=True,max_length=255)
    def __str__(self):
            return str(self.author)


class Document(models.Model):
    name=models.CharField(max_length=255)
    file = models.FileField()

    def __str__(self):
        return self.name