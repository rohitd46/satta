from ast import mod
from django.db import models
from django.contrib.auth.models import User

class Images(models.Model):
   image=models.FileField(upload_to="media/image")
   
class Profile(models.Model):
   user=models.OneToOneField(User,on_delete= models.CASCADE)
   forget_password_token=models.CharField(max_length=100)
   created_at=models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
        return self.user.username
   


class POINTS(models.Model):
   points=models.IntegerField(default=5)
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   
   def __str__(self):
        return self.user.first_name 
     
class MANAGEBANK(models.Model):
   GooglePayNumber=models.CharField(max_length=10)
   PhonePayNumber=models.CharField(max_length=10)
   PayTmNUmber=models.CharField(max_length=10)
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   
   def __str__(self):
        return self.user.first_name

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
     
class Kalyan_MorningSingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_MorningJodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_MorningSinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_MorningDoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_MorningTriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_MorningHalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_MorningFullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_MorningSingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_MorningJodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_MorningSinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_MorningDoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_MorningTriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_MorningHalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_MorningFullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class SrideviSingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class SrideviJodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class SrideviSinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class SrideviDoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class SrideviTriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class SrideviHalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class SrideviFullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Time_Bazar_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Time_Bazar_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Time_Bazar_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Time_Bazar_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Time_Bazar_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Time_Bazar_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Time_Bazar_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Day_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Day_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Day_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Day_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Day_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Day_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Day_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Kalyan_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class  New_Kalyan_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class  New_Kalyan_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class  New_Kalyan_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class  New_Kalyan_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class  New_Kalyan_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Kalyan_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Day_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Day_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Day_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Day_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Day_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Day_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Day_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Day_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Day_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Day_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Day_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Day_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Day_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Day_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Day_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Day_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Day_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Day_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Day_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Day_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Day_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Sridevi_Night_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Sridevi_Night_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Sridevi_Night_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Sridevi_Night_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Sridevi_Night_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Sridevi_Night_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Sridevi_Night_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Night_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Night_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Night_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Night_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Night_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Night_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Madhur_Night_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Main_Mumbai_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Main_Mumbai_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Main_Mumbai_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Main_Mumbai_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Main_Mumbai_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Main_Mumbai_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class New_Main_Mumbai_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Night_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Night_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Night_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Night_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Night_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Night_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Supreme_Night_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Night_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Night_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Night_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Night_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Night_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Night_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Milan_Night_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_Night_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_Night_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_Night_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_Night_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_Night_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_Night_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Kalyan_Night_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Night_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Night_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Night_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Night_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Night_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Night_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Rajdhani_Night_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Main_Bazar_SingleDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Main_Bazar_JodiDigit(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     digit=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Main_Bazar_SinglePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Main_Bazar_DoublePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Main_Bazar_TriplePana(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Main_Bazar_HalfSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     session = models.CharField(max_length=10)
     open_digit=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name

class Main_Bazar_FullSangam(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     date=models.DateField()
     open_pana=models.IntegerField(null=True)
     close_pana=models.IntegerField(null=True)
     points=models.IntegerField(null=True)
     
     def __str__(self):
        return self.user.first_name
# staline Time
class Ten_AM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name


class Ten_AM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Ten_AM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Ten_AM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Eleven_AM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Eleven_AM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Eleven_AM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Eleven_AM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Twelve_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Twelve_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Twelve_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Twelve_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class One_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class One_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class One_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class One_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Two_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Two_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Two_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Two_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Three_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Three_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Three_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Three_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Four_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Four_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Four_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Four_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Five_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Five_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Five_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Five_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Six_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Six_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Six_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Six_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Seven_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Seven_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Seven_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Seven_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Eight_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Eight_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Eight_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Eight_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Nine_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Nine_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Nine_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Nine_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Ten_PM_SingleDigit(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Ten_PM_SinglePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Ten_PM_DoublePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Ten_PM_TriplePana(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   pana=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Disawar(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name
   
class Faridabaad(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Gali(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name

class Gaziabaad(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   date=models.DateField()
   digit=models.IntegerField(null=True)
   points=models.IntegerField(null=True)
     
   def __str__(self):
      return self.user.first_name