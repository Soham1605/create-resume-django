from django.db import models

#Create your models here

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin_url = models.URLField()

class Experience(models.Model):
    TYPE_CHOICES = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
        ('certificate', 'Certificate'),
        ('skill', 'Skill'),
    ]
    
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


