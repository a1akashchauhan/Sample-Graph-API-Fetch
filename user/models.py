from django.db import models

class users(models.Model):
    UID = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    username= models.CharField(max_length=50)




class SocialMediaTokens(models.Model):
    UID= models.ForeignKey(users, on_delete= models.CASCADE)
    platform_name= models.CharField(max_length= 50)
    access_token= models.CharField(max_length=255)
    expiry_date= models.DateField()
    refresh_token = models.CharField(max_length=255)



class Analytics(models.Model):
    UID = models.ForeignKey(users, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=100)
    total_views = models.IntegerField(default=0)
    growth_rate = models.FloatField(default=0.0)
    total_followers = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)



