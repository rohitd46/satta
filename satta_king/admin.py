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
    list_display=( 'title','Open_Time')
    list_filter=('title',)
    search_fields=('title', )
admin.site.register(StarlineTime,StarlineTimeAdmin)

class GaliDisawarTimeAdmin(admin.ModelAdmin):
    list_display=( 'title','Open_Time')
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

admin.site.register(New_Main_Mumbai_SingleDigit)
admin.site.register(New_Main_Mumbai_JodiDigit)
admin.site.register(New_Main_Mumbai_SinglePana)
admin.site.register(New_Main_Mumbai_DoublePana)
admin.site.register(New_Main_Mumbai_TriplePana)
admin.site.register(New_Main_Mumbai_HalfSangam)
admin.site.register(New_Main_Mumbai_FullSangam)

admin.site.register(Supreme_Night_SingleDigit)
admin.site.register(Supreme_Night_JodiDigit)
admin.site.register(Supreme_Night_SinglePana)
admin.site.register(Supreme_Night_DoublePana)
admin.site.register(Supreme_Night_TriplePana)
admin.site.register(Supreme_Night_HalfSangam)
admin.site.register(Supreme_Night_FullSangam)

admin.site.register(Milan_Night_SingleDigit)
admin.site.register(Milan_Night_JodiDigit)
admin.site.register(Milan_Night_SinglePana)
admin.site.register(Milan_Night_DoublePana)
admin.site.register(Milan_Night_TriplePana)
admin.site.register(Milan_Night_HalfSangam)
admin.site.register(Milan_Night_FullSangam)

admin.site.register(Kalyan_Night_SingleDigit)
admin.site.register(Kalyan_Night_JodiDigit)
admin.site.register(Kalyan_Night_SinglePana)
admin.site.register(Kalyan_Night_DoublePana)
admin.site.register(Kalyan_Night_TriplePana)
admin.site.register(Kalyan_Night_HalfSangam)
admin.site.register(Kalyan_Night_FullSangam)

admin.site.register(Rajdhani_Night_SingleDigit)
admin.site.register(Rajdhani_Night_JodiDigit)
admin.site.register(Rajdhani_Night_SinglePana)
admin.site.register(Rajdhani_Night_DoublePana)
admin.site.register(Rajdhani_Night_TriplePana)
admin.site.register(Rajdhani_Night_HalfSangam)
admin.site.register(Rajdhani_Night_FullSangam)

admin.site.register(Main_Bazar_SingleDigit)
admin.site.register(Main_Bazar_JodiDigit)
admin.site.register(Main_Bazar_SinglePana)
admin.site.register(Main_Bazar_DoublePana)
admin.site.register(Main_Bazar_TriplePana)
admin.site.register(Main_Bazar_HalfSangam)
admin.site.register(Main_Bazar_FullSangam)

admin.site.register(Ten_AM_SingleDigit)
admin.site.register(Ten_AM_SinglePana)
admin.site.register(Ten_AM_DoublePana)
admin.site.register(Ten_AM_TriplePana)

admin.site.register(Eleven_AM_SingleDigit)
admin.site.register(Eleven_AM_SinglePana)
admin.site.register(Eleven_AM_DoublePana)
admin.site.register(Eleven_AM_TriplePana)

admin.site.register(Twelve_PM_SingleDigit)
admin.site.register(Twelve_PM_SinglePana)
admin.site.register(Twelve_PM_DoublePana)
admin.site.register(Twelve_PM_TriplePana)

admin.site.register(One_PM_SingleDigit)
admin.site.register(One_PM_SinglePana)
admin.site.register(One_PM_DoublePana)
admin.site.register(One_PM_TriplePana)

admin.site.register(Two_PM_SingleDigit)
admin.site.register(Two_PM_SinglePana)
admin.site.register(Two_PM_DoublePana)
admin.site.register(Two_PM_TriplePana)

admin.site.register(Three_PM_SingleDigit)
admin.site.register(Three_PM_SinglePana)
admin.site.register(Three_PM_DoublePana)
admin.site.register(Three_PM_TriplePana)

admin.site.register(Four_PM_SingleDigit)
admin.site.register(Four_PM_SinglePana)
admin.site.register(Four_PM_DoublePana)
admin.site.register(Four_PM_TriplePana)

admin.site.register(Five_PM_SingleDigit)
admin.site.register(Five_PM_SinglePana)
admin.site.register(Five_PM_DoublePana)
admin.site.register(Five_PM_TriplePana)

admin.site.register(Six_PM_SingleDigit)
admin.site.register(Six_PM_SinglePana)
admin.site.register(Six_PM_DoublePana)
admin.site.register(Six_PM_TriplePana)

admin.site.register(Seven_PM_SingleDigit)
admin.site.register(Seven_PM_SinglePana)
admin.site.register(Seven_PM_DoublePana)
admin.site.register(Seven_PM_TriplePana)

class Enight_PM_DoublePanaAdmin(admin.ModelAdmin):
    list_display=('user','date','pana','points' )
    search_fields=('date', )
    list_filter=('date',)
    list_per_page= 10
    

admin.site.register(Eight_PM_SingleDigit)
admin.site.register(Eight_PM_SinglePana)
admin.site.register(Eight_PM_DoublePana,Enight_PM_DoublePanaAdmin)
admin.site.register(Eight_PM_TriplePana)

admin.site.register(Nine_PM_SingleDigit)
admin.site.register(Nine_PM_SinglePana)
admin.site.register(Nine_PM_DoublePana)
admin.site.register(Nine_PM_TriplePana)

admin.site.register(Ten_PM_SingleDigit)
admin.site.register(Ten_PM_SinglePana)
admin.site.register(Ten_PM_DoublePana)
admin.site.register(Ten_PM_TriplePana)

admin.site.register(Gali)
admin.site.register(Disawar)
admin.site.register(Faridabaad)
admin.site.register(Gaziabaad)