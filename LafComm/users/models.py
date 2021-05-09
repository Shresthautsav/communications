from django.db import models
from postgres_copy import CopyManager

class Department(models.Model):
    major=models.CharField(max_length=50)
    objects = CopyManager()
    def __str__(self):
        return self.major

class NewsletterSection(models.Model):
    section_name=models.CharField(max_length=50)
    objects = CopyManager()
    def __str__(self):
        return self.section_name

# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICES =(
        ('Student','Student'),
        ('Alumni','Alumni'),
        ('Faculty','Faculty'),
        ('Staff','Staff'),
        ('Par_Fam','Parent/Family'),
        ('CHC','College Hill Community'),
        ('Other','Other'),
        )
    email = models.EmailField()
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    preferred_name = models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=20,blank=True)
    relation_to_college=models.CharField(max_length=50,choices=USER_TYPE_CHOICES,blank=True,null=True)
    class_year=models.CharField(max_length=10,blank=True)
    department=models.ManyToManyField(Department,blank=True)
    interest_newsletter=models.ManyToManyField(NewsletterSection,blank=True)

    objects = CopyManager()

    def __str__(self):
        return self.first_name

    
    
