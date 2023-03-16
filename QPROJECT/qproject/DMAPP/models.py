from django.db import models

# Create your models here.
class user(models.Model):
    company_name=models.CharField(max_length=20)
    company_logo=models.ImageField()
    username=models.CharField(max_length=20)
    password = models.CharField(max_length=120)



class login(models.Model):
    username=models.CharField(max_length=20)
    password = models.CharField(max_length=120)


class task_creation(models.Model):
    company_name=models.CharField(max_length=20)
    company_logo=models.ImageField()
    campaign_name=models.CharField(max_length=20)
    start_date=models.CharField(max_length=20)
    end_date=models.CharField(max_length=20)
    planned_impressions=models.IntegerField()
    planned_clicks=models.IntegerField()
    planned_cost=models.IntegerField()

