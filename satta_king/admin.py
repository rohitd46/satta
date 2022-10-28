from django.contrib import admin
from satta_king.models import *

# Register your models here.
admin.site.register(POINTS)
admin.site.register(MANAGEBANK)
admin.site.register(Images)
admin.site.register(Profile)


class DailyTimeAdmin(admin.ModelAdmin):
    list_display=( 'title','Opne_Time','Close_Time')

admin.site.register(DailyTime,DailyTimeAdmin)

class DailyBazarAdmin(admin.ModelAdmin):
    list_display=( 'title','Date','Number')
    list_filter=('Date','title')
    search_fields=('title', )


admin.site.register(DailyBazar,DailyBazarAdmin)

class StarlineAdmin(admin.ModelAdmin):
    list_display=( 'title','Date','Number')
    list_filter=('Date','title')
    search_fields=('title', )


admin.site.register(Starline,StarlineAdmin)

class GaliDisawarAdmin(admin.ModelAdmin):
    list_display=( 'title','Date','Number')
    list_filter=('Date','title')
    search_fields=('title', )


admin.site.register(GaliDisawar,GaliDisawarAdmin)

class StarlineTimeAdmin(admin.ModelAdmin):
    list_display=( 'title','Open_Time','Close_Time')
    list_filter=('title',)
    search_fields=('title', )
admin.site.register(StarlineTime,StarlineTimeAdmin)

class GaliDisawarTimeAdmin(admin.ModelAdmin):
    list_display=( 'title','Open_Time','Close_Time')
    list_filter=('title',)
    search_fields=('title', )
admin.site.register(GaliDisawarTime,GaliDisawarTimeAdmin)

class Milan_MorningSingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_MorningSingleDigit,Milan_MorningSingleDigitAdmin)

class Milan_MorningJodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_MorningJodiDigit,Milan_MorningJodiDigitAdmin)

class Milan_MorningSinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_MorningSinglePana,Milan_MorningSinglePanaAdmin)

class Milan_MorningDoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_MorningDoublePana,Milan_MorningDoublePanaAdmin)

class Milan_MorningTriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_MorningTriplePana,Milan_MorningTriplePanaAdmin)

class Milan_MorningHalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_MorningHalfSangam,Milan_MorningHalfSangamAdmin)

class Milan_MorningFullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_MorningFullSangam,Milan_MorningFullSangamAdmin)

class Welcome_MorningSingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Welcome_MorningSingleDigit,Welcome_MorningSingleDigitAdmin)
class Welcome_MorningJodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Welcome_MorningJodiDigit,Welcome_MorningJodiDigitAdmin)
class Welcome_MorningSinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Welcome_MorningSinglePana,Welcome_MorningSinglePanaAdmin)
class Welcome_MorningDoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Welcome_MorningDoublePana,Welcome_MorningDoublePanaAdmin)

class Welcome_MorningTriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Welcome_MorningTriplePana,Welcome_MorningTriplePanaAdmin)

class Welcome_MorningHalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Welcome_MorningHalfSangam,Welcome_MorningHalfSangamAdmin)

class Welcome_MorningFullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Welcome_MorningFullSangam,Welcome_MorningFullSangamAdmin)

class Kalyan_MorningSingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_MorningSingleDigit,Kalyan_MorningSingleDigitAdmin)

class Kalyan_MorningJodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_MorningJodiDigit,Kalyan_MorningJodiDigitAdmin)

class Kalyan_MorningSinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_MorningSinglePana,Kalyan_MorningSinglePanaAdmin)

class Kalyan_MorningDoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_MorningDoublePana,Kalyan_MorningDoublePanaAdmin)

class Kalyan_MorningTriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_MorningTriplePana,Kalyan_MorningTriplePanaAdmin)

class Kalyan_MorningHalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_MorningHalfSangam,Kalyan_MorningHalfSangamAdmin)

class Kalyan_MorningFullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_MorningFullSangam,Kalyan_MorningFullSangamAdmin)

class Madhur_MorningSingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_MorningSingleDigit,Madhur_MorningSingleDigitAdmin)

class Madhur_MorningJodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_MorningJodiDigit,Madhur_MorningJodiDigitAdmin)

class Madhur_MorningSinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_MorningSinglePana,Madhur_MorningSinglePanaAdmin)

class Madhur_MorningDoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_MorningDoublePana,Madhur_MorningDoublePanaAdmin)

class Madhur_MorningTriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_MorningTriplePana,Madhur_MorningTriplePanaAdmin)

class Madhur_MorningHalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_MorningHalfSangam,Madhur_MorningHalfSangamAdmin)

class Madhur_MorningFullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_MorningFullSangam,Madhur_MorningFullSangamAdmin)

class SrideviSingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(SrideviSingleDigit,SrideviSingleDigitAdmin)

class SrideviJodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(SrideviJodiDigit,SrideviJodiDigitAdmin)
class SrideviSinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(SrideviSinglePana,SrideviSinglePanaAdmin)

class SrideviDoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(SrideviDoublePana,SrideviDoublePanaAdmin)

class SrideviTriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(SrideviTriplePana,SrideviTriplePanaAdmin)

class SrideviHalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(SrideviHalfSangam,SrideviHalfSangamAdmin)
class SrideviFullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(SrideviFullSangam,SrideviFullSangamAdmin)

class Time_Bazar_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Time_Bazar_SingleDigit,Time_Bazar_SingleDigitAdmin)

class Time_Bazar_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Time_Bazar_JodiDigit,Time_Bazar_JodiDigitAdmin)

class Time_Bazar_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Time_Bazar_SinglePana,Time_Bazar_SinglePanaAdmin)

class Time_Bazar_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Time_Bazar_DoublePana,Time_Bazar_DoublePanaAdmin)

class Time_Bazar_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Time_Bazar_TriplePana,Time_Bazar_TriplePanaAdmin)

class Time_Bazar_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Time_Bazar_HalfSangam,Time_Bazar_HalfSangamAdmin)

class Time_Bazar_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Time_Bazar_FullSangam,Time_Bazar_FullSangamAdmin)

class Madhur_Day_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Day_SingleDigit,Madhur_Day_SingleDigitAdmin)

class Madhur_Day_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Day_JodiDigit,Madhur_Day_JodiDigitAdmin)

class Madhur_Day_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Day_SinglePana,Madhur_Day_SinglePanaAdmin)

class Madhur_Day_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Day_DoublePana,Madhur_Day_DoublePanaAdmin)

class Madhur_Day_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Day_TriplePana,Madhur_Day_TriplePanaAdmin)

class Madhur_Day_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Day_HalfSangam,Madhur_Day_HalfSangamAdmin)

class Madhur_Day_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Day_FullSangam,Madhur_Day_FullSangamAdmin)

class New_Kalyan_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Kalyan_SingleDigit,New_Kalyan_SingleDigitAdmin)

class New_Kalyan_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Kalyan_JodiDigit, New_Kalyan_JodiDigitAdmin)

class New_Kalyan_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Kalyan_SinglePana,New_Kalyan_SinglePanaAdmin)
class New_Kalyan_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Kalyan_DoublePana,New_Kalyan_DoublePanaAdmin)

class New_Kalyan_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Kalyan_TriplePana,New_Kalyan_TriplePanaAdmin)
class New_Kalyan_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Kalyan_HalfSangam, New_Kalyan_HalfSangamAdmin)

class New_Kalyan_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Kalyan_FullSangam,New_Kalyan_FullSangamAdmin)

class Milan_Day_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Day_SingleDigit,Milan_Day_SingleDigitAdmin)

class Milan_Day_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Day_JodiDigit,Milan_Day_JodiDigitAdmin)

class Milan_Day_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Day_SinglePana,Milan_Day_SinglePanaAdmin)

class Milan_Day_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Day_DoublePana,Milan_Day_DoublePanaAdmin)

class Milan_Day_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Day_TriplePana, Milan_Day_TriplePanaAdmin)

class Milan_Day_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Day_HalfSangam,Milan_Day_HalfSangamAdmin)

class Milan_Day_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Day_FullSangam,Milan_Day_FullSangamAdmin)

class Rajdhani_Day_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Day_SingleDigit,Rajdhani_Day_SingleDigitAdmin)

class Rajdhani_Day_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Day_JodiDigit,Rajdhani_Day_JodiDigitAdmin)

class Rajdhani_Day_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Day_SinglePana,Rajdhani_Day_SinglePanaAdmin)

class Rajdhani_Day_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Day_DoublePana,Rajdhani_Day_DoublePanaAdmin)

class Rajdhani_Day_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Day_TriplePana,Rajdhani_Day_TriplePanaAdmin)

class Rajdhani_Day_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Day_HalfSangam,Rajdhani_Day_HalfSangamAdmin)

class Rajdhani_Day_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Day_FullSangam,Rajdhani_Day_FullSangamAdmin)

class Supreme_Day_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Day_SingleDigit,Supreme_Day_SingleDigitAdmin)

class Supreme_Day_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Day_JodiDigit,Supreme_Day_JodiDigitAdmin)

class Supreme_Day_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Day_SinglePana,Supreme_Day_SinglePanaAdmin)

class Supreme_Day_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Day_DoublePana,Supreme_Day_DoublePanaAdmin)

class Supreme_Day_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Day_TriplePana,Supreme_Day_TriplePanaAdmin)

class Supreme_Day_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Day_HalfSangam,Supreme_Day_HalfSangamAdmin)

class Supreme_Day_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Day_FullSangam,Supreme_Day_FullSangamAdmin)

class Kalyan_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_SingleDigit,Kalyan_SingleDigitAdmin)

class Kalyan_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_JodiDigit)

class Kalyan_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_SinglePana,Kalyan_SinglePanaAdmin)

class Kalyan_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_DoublePana,Kalyan_DoublePanaAdmin)

class Kalyan_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_TriplePana,Kalyan_TriplePanaAdmin)

class Kalyan_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_HalfSangam, Kalyan_HalfSangamAdmin)

class Kalyan_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_FullSangam,Kalyan_FullSangamAdmin)

class Sridevi_Night_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Sridevi_Night_SingleDigit,Sridevi_Night_SingleDigitAdmin)

class Sridevi_Night_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Sridevi_Night_JodiDigit,Sridevi_Night_JodiDigitAdmin)

class Sridevi_Night_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Sridevi_Night_SinglePana,Sridevi_Night_SinglePanaAdmin)

class Sridevi_Night_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Sridevi_Night_DoublePana,Sridevi_Night_DoublePanaAdmin)

class Sridevi_Night_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Sridevi_Night_TriplePana,Sridevi_Night_TriplePanaAdmin)

class Sridevi_Night_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Sridevi_Night_HalfSangam,Sridevi_Night_HalfSangamAdmin)

class Sridevi_Night_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Sridevi_Night_FullSangam,Sridevi_Night_FullSangamAdmin)

class Madhur_Night_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Night_SingleDigit,Madhur_Night_SingleDigitAdmin)

class Madhur_Night_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Night_JodiDigit,Madhur_Night_JodiDigitAdmin)

class Madhur_Night_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Night_SinglePana,Madhur_Night_SinglePanaAdmin)

class Madhur_Night_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Night_DoublePana,Madhur_Night_DoublePanaAdmin)

class Madhur_Night_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Night_TriplePana,Madhur_Night_TriplePanaAdmin)

class Madhur_Night_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Madhur_Night_HalfSangam,Madhur_Night_HalfSangamAdmin)
                    
class Madhur_Night_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10                   
admin.site.register(Madhur_Night_FullSangam,Madhur_Night_FullSangamAdmin)


class New_Main_Mumbai_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(New_Main_Mumbai_SingleDigit,New_Main_Mumbai_SingleDigitAdmin)

class New_Main_Mumbai_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Main_Mumbai_JodiDigit,New_Main_Mumbai_JodiDigitAdmin)

class New_Main_Mumbai_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Main_Mumbai_SinglePana,New_Main_Mumbai_SinglePanaAdmin)

class New_Main_Mumbai_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Main_Mumbai_DoublePana,New_Main_Mumbai_DoublePanaAdmin)

class New_Main_Mumbai_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(New_Main_Mumbai_TriplePana,New_Main_Mumbai_TriplePanaAdmin)

class New_Main_Mumbai_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(New_Main_Mumbai_HalfSangam,New_Main_Mumbai_HalfSangamAdmin)

class New_Main_Mumbai_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(New_Main_Mumbai_FullSangam,New_Main_Mumbai_FullSangamAdmin)

class Supreme_Night_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Night_SingleDigit,Supreme_Night_SingleDigitAdmin)

class Supreme_Night_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Night_JodiDigit,Supreme_Night_JodiDigitAdmin)

class Supreme_Night_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Night_SinglePana,Supreme_Night_SinglePanaAdmin)

class Supreme_Night_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Night_DoublePana,Supreme_Night_DoublePanaAdmin)

class Supreme_Night_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Night_TriplePana,Supreme_Night_TriplePanaAdmin)

class Supreme_Night_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Supreme_Night_HalfSangam,Supreme_Night_HalfSangamAdmin)

class Supreme_Night_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Supreme_Night_FullSangam,Supreme_Night_FullSangamAdmin)


class Milan_Night_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Night_SingleDigit,Milan_Night_SingleDigitAdmin)

class Milan_Night_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Night_JodiDigit,Milan_Night_JodiDigitAdmin)

class Milan_Night_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Night_SinglePana,Milan_Night_SinglePanaAdmin)

class Milan_Night_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Milan_Night_DoublePana,Milan_Night_DoublePanaAdmin)

class Milan_Night_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Milan_Night_TriplePana,Milan_Night_TriplePanaAdmin)

class Milan_Night_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Milan_Night_HalfSangam,Milan_Night_HalfSangamAdmin)

class Milan_Night_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Milan_Night_FullSangam,Milan_Night_FullSangamAdmin)

class Kalyan_Night_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_Night_SingleDigit,Kalyan_Night_SingleDigitAdmin)

class Kalyan_Night_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_Night_JodiDigit,Kalyan_Night_JodiDigitAdmin)

class Kalyan_Night_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_Night_SinglePana,Kalyan_Night_SinglePanaAdmin)

class Kalyan_Night_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_Night_DoublePana,Kalyan_Night_DoublePanaAdmin)

class Kalyan_Night_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Kalyan_Night_TriplePana,Kalyan_Night_TriplePanaAdmin)

class Kalyan_Night_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Kalyan_Night_HalfSangam,Kalyan_Night_HalfSangamAdmin)

class Kalyan_Night_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Kalyan_Night_FullSangam,Kalyan_Night_FullSangamAdmin)

class Rajdhani_Night_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Night_SingleDigit,Rajdhani_Night_SingleDigitAdmin)

class Rajdhani_Night_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Night_JodiDigit,Rajdhani_Night_JodiDigitAdmin)

class Rajdhani_Night_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Night_SinglePana,Rajdhani_Night_SinglePanaAdmin)

class Rajdhani_Night_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Night_DoublePana,Rajdhani_Night_DoublePanaAdmin)
class Rajdhani_Night_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Rajdhani_Night_TriplePana,Rajdhani_Night_TriplePanaAdmin)

class Rajdhani_Night_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Rajdhani_Night_HalfSangam,Rajdhani_Night_HalfSangamAdmin)
class Rajdhani_Night_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Rajdhani_Night_FullSangam,Rajdhani_Night_FullSangamAdmin)

class Main_Bazar_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Main_Bazar_SingleDigit,Main_Bazar_SingleDigitAdmin)

class Main_Bazar_JodiDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Main_Bazar_JodiDigit,Main_Bazar_JodiDigitAdmin)
class Main_Bazar_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Main_Bazar_SinglePana,Main_Bazar_SinglePanaAdmin)

class Main_Bazar_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Main_Bazar_DoublePana,Main_Bazar_DoublePanaAdmin)
class Main_Bazar_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Main_Bazar_TriplePana,Main_Bazar_TriplePanaAdmin)
class Main_Bazar_HalfSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_digit','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Main_Bazar_HalfSangam, Main_Bazar_HalfSangamAdmin)

class Main_Bazar_FullSangamAdmin(admin.ModelAdmin):
    list_display=('user','date','open_pana','close_pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10          
admin.site.register(Main_Bazar_FullSangam,Main_Bazar_FullSangamAdmin)

class Ten_AM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_AM_SingleDigit,Ten_AM_SingleDigitAdmin)
class Ten_AM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_AM_SinglePana,Ten_AM_SinglePanaAdmin)
class Ten_AM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_AM_DoublePana,Ten_AM_DoublePanaAdmin)
class Ten_AM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_AM_TriplePana,Ten_AM_TriplePanaAdmin)

class Eleven_AM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eleven_AM_SingleDigit,Eleven_AM_SingleDigitAdmin)
class Eleven_AM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eleven_AM_SinglePana,Eleven_AM_SinglePanaAdmin)
class Eleven_AM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eleven_AM_DoublePana,Eleven_AM_DoublePanaAdmin)
class Eleven_AM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eleven_AM_TriplePana, Eleven_AM_TriplePanaAdmin)

class Twelve_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Twelve_PM_SingleDigit,Twelve_PM_SingleDigitAdmin)
class Twelve_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Twelve_PM_SinglePana,Twelve_PM_SinglePanaAdmin)
class Twelve_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Twelve_PM_DoublePana,Twelve_PM_DoublePanaAdmin)
class Twelve_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Twelve_PM_TriplePana,Twelve_PM_TriplePanaAdmin)

class One_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(One_PM_SingleDigit,One_PM_SingleDigitAdmin)
class One_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(One_PM_SinglePana, One_PM_SinglePanaAdmin)
class One_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(One_PM_DoublePana, One_PM_DoublePanaAdmin)
class One_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(One_PM_TriplePana,One_PM_TriplePanaAdmin)

class Two_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Two_PM_SingleDigit,Two_PM_SingleDigitAdmin)

class Two_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Two_PM_SinglePana,Two_PM_SinglePanaAdmin)
class Two_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Two_PM_DoublePana,Two_PM_DoublePanaAdmin)

class Two_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Two_PM_TriplePana,Two_PM_TriplePanaAdmin)

class Three_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Three_PM_SingleDigit,Three_PM_SingleDigitAdmin)

class Three_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Three_PM_SinglePana,Three_PM_SinglePanaAdmin)
class Three_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Three_PM_DoublePana,Three_PM_DoublePanaAdmin)
class Three_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Three_PM_TriplePana,Three_PM_TriplePanaAdmin)

class Four_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Four_PM_SingleDigit,Four_PM_SingleDigitAdmin)
class Four_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Four_PM_SinglePana,Four_PM_SinglePanaAdmin)
class Four_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Four_PM_DoublePana,Four_PM_DoublePanaAdmin)
class Four_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Four_PM_TriplePana,Four_PM_TriplePanaAdmin)

class Five_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Five_PM_SingleDigit,Five_PM_SingleDigitAdmin)
class Five_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Five_PM_SinglePana, Five_PM_SinglePanaAdmin)
class Five_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Five_PM_DoublePana,Five_PM_DoublePanaAdmin)
class Five_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Five_PM_TriplePana,Five_PM_TriplePanaAdmin)

class Six_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Six_PM_SingleDigit,Six_PM_SingleDigitAdmin)
class Six_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Six_PM_SinglePana,Six_PM_SinglePanaAdmin)
class Six_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Six_PM_DoublePana,Six_PM_DoublePanaAdmin)
class Six_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Six_PM_TriplePana,Six_PM_TriplePanaAdmin)

class Seven_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Seven_PM_SingleDigit,Seven_PM_SingleDigitAdmin)
class Seven_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Seven_PM_SinglePana,Seven_PM_SinglePanaAdmin)
class Seven_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Seven_PM_DoublePana,Seven_PM_DoublePanaAdmin)
class Seven_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Seven_PM_TriplePana,Seven_PM_TriplePanaAdmin)

class Enight_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eight_PM_DoublePana,Enight_PM_DoublePanaAdmin)    
class Eight_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eight_PM_SingleDigit,Eight_PM_SingleDigitAdmin)

class Eight_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eight_PM_SinglePana,Eight_PM_SinglePanaAdmin)

class Eight_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Eight_PM_TriplePana,Eight_PM_TriplePanaAdmin)

class Nine_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Nine_PM_SingleDigit,Nine_PM_SingleDigitAdmin)

class Nine_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Nine_PM_SinglePana,Nine_PM_SinglePanaAdmin)

class Nine_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Nine_PM_DoublePana,Nine_PM_DoublePanaAdmin)

class Nine_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Nine_PM_TriplePana,Nine_PM_TriplePanaAdmin)
class Ten_PM_SingleDigitAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_PM_SingleDigit,Ten_PM_SingleDigitAdmin)
class Ten_PM_SinglePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_PM_SinglePana,Ten_PM_SinglePanaAdmin)
class Ten_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_PM_DoublePana,Ten_PM_DoublePanaAdmin)
class Ten_PM_TriplePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Ten_PM_TriplePana,Ten_PM_TriplePanaAdmin)

class GaliAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Gali,GaliAdmin)

class DisawarAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Disawar,DisawarAdmin)
class FaridabaadAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Faridabaad,FaridabaadAdmin)

class GaziabaadAdmin(admin.ModelAdmin):
    list_display=('user','date','digit','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
admin.site.register(Gaziabaad,GaziabaadAdmin)