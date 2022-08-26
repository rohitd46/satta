from django.db import models
from django.contrib.auth.models import User

class POINTS(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   points=models.IntegerField(default=5)

class Milan_MorningSingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_MorningJodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_MorningSinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_MorningDoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_MorningTriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_MorningHalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_MorningFullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name
    
class Welcome_MorningSingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Welcome_MorningJodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Welcome_MorningSinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Welcome_MorningDoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Welcome_MorningTriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Welcome_MorningHalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Welcome_MorningFullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name
