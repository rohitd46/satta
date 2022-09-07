from http import client
from turtle import update
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import *
import razorpay
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .helpes import send_forget_password_mail
import uuid




def Login(request):
    if request.method == "POST":
        phonenumber=request.POST.get('username')
        password=request.POST.get('password')
        
        user = auth.authenticate(username=phonenumber,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid Username/Password")
            return redirect("login")
    else:   
        return render(request,'login.html')

def SignUp(request):
    if request.method =='POST':
        name=request.POST.get('first_name')
        phonenumber=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        if password==repassword:
            if User.objects.filter(username=phonenumber ).exists():
                messages.info(request,"Username Already Exists.")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists.")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=phonenumber,first_name=name,email=email,password=password)
                user.save()
                points=request.POST.get('points')
                userpoint=POINTS(points=points,user=user)
                userpoint.save()
                send_mail(
                    'Account Create',
                    f'Welcome {user.first_name} to Online Satta King.Your Account Has Create Secessfully.Your Joinning Bounus {userpoint.points} Points Credit in Your Account',
                    'onlinesattaking83@gmail.com',
                    [email],
                    fail_silently=False,
                    )
                messages.info(request,"Account Created.")
                return redirect('home')
        else:
            messages.info(request,"password mismatch")
            return redirect('signup')
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')




def ForgetPassword(request):
    if request.method=="POST":
        username=request.POST.get('username')
        
        if not User.objects.filter(username=username).first():
            messages.info(request,"No User Found with this Phone Number.")
            return redirect('forgetpassword')
        
        user_obj=User.objects.get(username=username)
        token=str(uuid.uuid4())
        print(user_obj)
        profile_obj=Profile.objects.get(user=user_obj)
        print(profile_obj)
        profile_obj.forget_password_token=token
        
        profile_obj.save()
        send_forget_password_mail(user_obj.email,token)
        messages.info(request,"Email Send To Your Register Email ID.")
        return redirect('forgetpassword')
            
    return render (request,'forgetpassword.html')

def ResetPassword(request, token):
    context={
        
    }
    profile_obj=Profile.objects.filter(forget_password_token=token).first()
    print(profile_obj)
    return render(request,'resetpassword.html')




@login_required(login_url='/')
def Home(request):
    return render(request,'index.html')

def Wallet(request):
    point=POINTS.objects.filter(user=request.user)
    return render (request,'wallet.html',{"point":point})

def Bank(request,):
    bank=MANAGEBANK.objects.filter(user=request.user)
    print(bank)
    data={
        'bank':bank
    }
    if request.method == "POST":
        user=request.user
        GooglePayNumber=request.POST.get('GooglePayNumber')
        PhonePayNumber=request.POST.get('PhonePayNumber')
        PayTmNUmber=request.POST.get('PayTmNUmber')
        addbank=MANAGEBANK(user=user,GooglePayNumber=GooglePayNumber,PhonePayNumber=PhonePayNumber,PayTmNUmber=PayTmNUmber)
        addbank.save()
        messages.info(request,"All Details Are save")
    return render (request,'manage_bank.html',data)

def Winning(request):
    return render (request,'winning_history.html')

def BID(request):
    return render (request,'bid_history.html')

def GamesRate(request):
    return render (request,'games_rate.html')

def Conatct(request):
    return render (request,'contact.html')

def ChangePassword(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            v=form.save()
            update_session_auth_hash(request,v)
            messages.info(request,"Password Change Sucessfully..")
    else:  
        form=PasswordChangeForm(request.user)
    parmas={
        'form': form
    }
    return render (request,'change_password.html',parmas)


def HowToPlay(request):
    return redirect('https://www.youtube.com')

def ADDPOINT(request):
    if request.method=="POST":
        user=request.user
        amount=int(request.POST.get('amount'))*100
        print(amount,user)
     
        client=razorpay.Client(auth=("rzp_test_z4jsh2NBxCwEns" ,"7HIjeNqkGiUoyvYkRVqVuguL"))
        payment=client.order.create({'amount' :amount,'currency': 'INR','payment_capture':'1'})
        payment_id=payment['id']
        # print(payment)
        context={
            'amount':amount,
            'order_id':payment_id
        }
        
        return render (request,'add_point.html',context)
    return render (request,'add_point.html')

def STARLINE(request):
    return render (request,'starline.html')

def GALIDISWAR(request):
    return render (request,'galidiswar.html')
# sidebar end
# MILAN MORNING START
def MILANMORING(request):
    return render (request,'MILANMORNING/millanmoring.html')

def MILANMORNINGSINGLEDIGIT(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        digit=request.POST.get('digit')
        points=request.POST.get('points')
        milanmorningsingledigit=Milan_MorningSingleDigit(user=user,session=session,digit=digit,points=points,date=datetime.today())
        milanmorningsingledigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('milan_morning')
    return render (request,'MILANMORNING/single_digit.html')

def MILANMORNINGJODIDIGIT(request):
     if request.method=="POST":
        user=request.user
        digit=request.POST.get('digit')
        points=request.POST.get('points')
        milanmorningjodidigit=Milan_MorningJodiDigit(user=user,digit=digit,points=points,date=datetime.today())
        milanmorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('milan_morning')
     return render (request,'MILANMORNING/jodi_digit.html')

def MILANMORNINGSINGLEPANNA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        milanmorningsinglepana=Milan_MorningSinglePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        milanmorningsinglepana.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('milan_morning')
    return render (request,'MILANMORNING/singlepanna.html')

def MILANMORNINGDOUBLEPANNA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        milanmorningdoublepana=Milan_MorningDoublePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        milanmorningdoublepana.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('milan_morning')
    return render (request,'MILANMORNING/doublepanna.html')

def MILANMORNINGTRIPLEPANNA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        milanmorningtriplepana=Milan_MorningTriplePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        milanmorningtriplepana.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('milan_morning')
    return render (request,'MILANMORNING/triplepanna.html')

def MILANMORNINGHALFSANGAM(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        open_digit=request.POST.get('open_digit')
        close_pana=request.POST.get('close_pana')
        points=request.POST.get('points')
        milanmorninghalfsangam=Milan_MorningHalfSangam(user=user,session=session,open_digit=open_digit,close_pana=close_pana,points=points,date=datetime.today())
        milanmorninghalfsangam.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('milan_morning')
    return render (request,'MILANMORNING/halfsangam.html')

def MILANMORNINGFULLSANGAM(request):
    if request.method=="POST":
        user=request.user
        open_pana=request.POST.get('open_pana')
        close_pana=request.POST.get('close_pana')
        points=request.POST.get('points')
        milanmorningfullsangam=Milan_MorningFullSangam(user=user,open_pana=open_pana,close_pana=close_pana,points=points,date=datetime.today())
        milanmorningfullsangam.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('milan_morning')
    return render (request,'MILANMORNING/fullsangam.html')
# MILAN MORNING END
# WELCOMR MORNING START
def WELCOMEMORNING(request):
    return render (request,'WELCOMEMORING/welcomemorning.html')

def WELCOMEMORNINGSINGLEDIGIT(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        digit=request.POST.get('digit')
        points=request.POST.get('points')
        welcomemorningsingledigit=Welcome_MorningSingleDigit(user=user,session=session,digit=digit,points=points,date=datetime.today())
        welcomemorningsingledigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('welcome_morning')
    return render (request,'WELCOMEMORING/welcomesingle_digit.html')

def WELCOMEMORNINGJODIDIGIT(request):
    if request.method=="POST":
        user=request.user
        digit=request.POST.get('digit')
        points=request.POST.get('points')
        welcomemorningjodidigit=Welcome_MorningJodiDigit(user=user,digit=digit,points=points,date=datetime.today())
        welcomemorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('welcome_morning')
    return render (request,'WELCOMEMORING/welcomejodi_digit.html')

def WELCOMEMORNINGSINGLEPANNA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        welcomemorningsinglepana=Welcome_MorningSinglePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        welcomemorningsinglepana.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('welcome_morning')
    return render (request,'WELCOMEMORING/singlepanna.html')

def WELCOMEMORNINGDOUBLEPANNA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        welcomemorningdoublepana=Welcome_MorningDoublePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        welcomemorningdoublepana.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('welcome_morning')
    return render (request,'WELCOMEMORING/doublepanna.html')

def WELCOMEMORNINGTRIPLEPANNA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        welcomemorningtriplepana=Welcome_MorningTriplePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        welcomemorningtriplepana.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('welcome_morning')
    return render (request,'WELCOMEMORING/triplepanna.html')

def WELCOMEMORNINGHALFSANGAM(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        open_digit=request.POST.get('open_digit')
        close_pana=request.POST.get('close_pana')
        points=request.POST.get('points')
        welcomemorninghalfsangam=Welcome_MorningHalfSangam(user=user,session=session,open_digit=open_digit,close_pana=close_pana,points=points,date=datetime.today())
        welcomemorninghalfsangam.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('welcome_morning')
    return render (request,'WELCOMEMORING/halfsangam.html')

def WELCOMEMORNINGFULLSANGAM(request):
    if request.method=="POST":
        user=request.user
        open_pana=request.POST.get('open_pana')
        close_pana=request.POST.get('close_pana')
        points=request.POST.get('points')
        welcomemorningfullsangam=Welcome_MorningFullSangam(user=user,open_pana=open_pana,close_pana=close_pana,points=points,date=datetime.today())
        welcomemorningfullsangam.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('welcome_morning')
    return render (request,'WELCOMEMORING/fullsangam.html')
# WELCOME MORNING END
# KALYAN MORNING START
def KALYANMORNING(request):
    return render (request,'KALYANMORNING/kalyanmorning.html')

def KALYANMORINGSINGLEDIGIT(request):
     if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        digit=request.POST.get('digit')
        points=request.POST.get('points')
        kalyanmorningsingledigit=Kalyan_MorningSingleDigit(user=user,session=session,digit=digit,points=points,date=datetime.today())
        kalyanmorningsingledigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('kalyan_morning')
     return render (request,'KALYANMORNING/single_digit.html')

def KALYANMORINGJODIDIGIT(request):
    if request.method=="POST":
        user=request.user
        digit=request.POST.get('digit')
        points=request.POST.get('points')
        kalyanmorningjodidigit=Kalyan_MorningJodiDigit(user=user,digit=digit,points=points,date=datetime.today())
        kalyanmorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('kalyan_morning')
    return render (request,'KALYANMORNING/jodi_digit.html')

def KALYANMORINGSINGLEPANA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        kalyanmorningjodidigit=Kalyan_MorningSinglePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        kalyanmorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('kalyan_morning')
    return render (request,'KALYANMORNING/singlepanna.html')

def KALYANMORINGDOUBLEPANA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        kalyanmorningjodidigit=Kalyan_MorningDoublePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        kalyanmorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('kalyan_morning')
    return render (request,'KALYANMORNING/doublepanna.html')

def KALYANMORNINGTRIPLEPANA(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        pana=request.POST.get('pana')
        points=request.POST.get('points')
        kalyanmorningjodidigit=Kalyan_MorningTriplePana(user=user,session=session,pana=pana,points=points,date=datetime.today())
        kalyanmorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('kalyan_morning')
    return render (request,'KALYANMORNING/triplepanna.html')

def KALYANMORINGJHALFSANGAM(request):
    if request.method=="POST":
        user=request.user
        session=request.POST.get('session')
        open_digit=request.POST.get('open_digit')
        close_pana=request.POST.get('close_pana')
        points=request.POST.get('points')
        kalyanmorningjodidigit=Kalyan_MorningHalfSangam(user=user,session=session,open_digit=open_digit,close_pana=close_pana,points=points,date=datetime.today())
        kalyanmorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('kalyan_morning')
    return render (request,'KALYANMORNING/halfsangam.html')

def KALYANMORINGFULLSANGAM(request):
     if request.method=="POST":
        user=request.user
        open_pana=request.POST.get('open_pana')
        close_pana=request.POST.get('close_pana')
        points=request.POST.get('points')
        kalyanmorningjodidigit=Kalyan_MorningFullSangam(user=user,open_pana=open_pana,close_pana=close_pana,points=points,date=datetime.today())
        kalyanmorningjodidigit.save()
        messages.info(request,"Your Bid Recived.Thank You!! ")
        return redirect('kalyan_morning')
     return render (request,'KALYANMORNING/fullsangam.html')
# KALYAN MORNING END
# MADHUR MORNING START
def MADHURMORNING(request):
    return render (request,'MADHURMORNING/madhurmorning.html')

def MADHURMORNINGSINGLEDIGIT(request):
    return render (request,'MADHURMORNING/single_digit.html')

def MADHURMORINGJODIDIGIT(request):
    return render (request,'MADHURMORNING/jodi_digit.html')

def MADHURMORINGSINGLEPANA(request):
    return render (request,'MADHURMORNING/singlepanna.html')

def MADHURMORINGDOUBLEPANA(request):
    return render (request,'MADHURMORNING/doublepanna.html')

def MADHURMORINGTRIPLEPANA(request):
    return render (request,'MADHURMORNING/triplepanna.html')

def MADHURMORINGHALFSANGAM(request):
    return render (request,'MADHURMORNING/halfsangam.html')

def MADHURMORINGFULLSANGAM(request):
    return render (request,'MADHURMORNING/fullsangam.html')
# MADHUR MORING END
# SRIDEVI START
def SRIDEVI(request):
    return render (request,'SRIDEVI/sridevi.html')

def SRIDEVISINGLEDIGIT(request):
    return render (request,'SRIDEVI/single_digit.html')

def SRIDEVIJODIDIGIT(request):
    return render (request,'SRIDEVI/jodi_digit.html')

def SRIDEVISINGLEPANA(request):
    return render (request,'SRIDEVI/singlepanna.html')

def SRIDEVIDOUBLEPANA(request):
    return render (request,'SRIDEVI/doublepanna.html')

def SRIDEVITRIPLEPANA(request):
    return render (request,'SRIDEVI/triplepanna.html')

def SRIDEVIHALFSANGAM(request):
    return render (request,'SRIDEVI/halfsangam.html')

def SRIDEVIFULLSANGAM(request):
    return render (request,'SRIDEVI/fullsangam.html')
# SRIDEVI END
# TIMEBAZAR START
def TIMEBAZAR(request):
    return render (request,'TIMEBAZAR/timebazar.html')

def TIMEBAZARSINGLEDIGIT(request):
    return render (request,'TIMEBAZAR/single_digit.html')

def TIMEBAZARJODIDIGIT(request):
    return render (request,'TIMEBAZAR/jodi_digit.html')

def TIMEBAZARSINGLEPANA(request):
    return render (request,'TIMEBAZAR/singlepanna.html')

def TIMEBAZARDOUBLEPANA(request):
    return render (request,'TIMEBAZAR/doublepanna.html')

def TIMEBAZARTRIPLEPANA(request):
    return render (request,'TIMEBAZAR/triplepanna.html')

def TIMEBAZARHALFSANGAM(request):
    return render (request,'TIMEBAZAR/halfsangam.html')

def TIMEBAZARFULLSANGAM(request):
    return render (request,'TIMEBAZAR/fullsangam.html')
# TIMEBAZAR END
#  MADHUR DAY START
def MADHURDAY(request):
    return render (request,'MADHURDAY/madhurday.html')

def MADHURDAYSINGLEDIGIT(request):
    return render (request,'MADHURDAY/single_digit.html')

def MADHURDAYJODIDIGIT(request):
    return render (request,'MADHURDAY/jodi_digit.html')

def MADHURDAYSINGLEPANA(request):
    return render (request,'MADHURDAY/singlepanna.html')

def MADHURDAYDOUBLEPANA(request):
    return render (request,'MADHURDAY/doublepanna.html')

def MADHURDAYTRIPLEPANA(request):
    return render (request,'MADHURDAY/triplepanna.html')

def MADHURDAYHALFSANGAM(request):
    return render (request,'MADHURDAY/halfsangam.html')

def MADHURDAYFULLSANGAM(request):
    return render (request,'MADHURDAY/fullsangam.html')
#  MADHUR DAY END
#  NEW KALYAN START
def NEWKALYAN(request):
    return render (request,'NEWKALYAN/newkalyan.html')

def NEWKALYANSINGLEDIGIT(request):
    return render (request,'NEWKALYAN/single_digit.html')

def NEWKALYANJODIDIGIT(request):
    return render (request,'NEWKALYAN/jodi_digit.html')

def NEWKALYANSINGLEPANA(request):
    return render (request,'NEWKALYAN/singlepanna.html')

def NEWKALYANDOUBLEPANA(request):
    return render (request,'NEWKALYAN/doublepanna.html')

def NEWKALYANTRIPLEPANA(request):
    return render (request,'NEWKALYAN/triplepanna.html')

def NEWKALYANHALFSANGAM(request):
    return render (request,'NEWKALYAN/halfsangam.html')

def NEWKALYANFULLSANGAM(request):
    return render (request,'NEWKALYAN/fullsangam.html')
#  NEW KALYAN END
#  MILANDAY START
def MILANDAY(request):
    return render (request,'MILANDAY/milanday.html')

def MILANDAYSINGLEDIGIT(request):
    return render (request,'MILANDAY/single_digit.html')

def MILANDAYJODIDIGIT(request):
    return render (request,'MILANDAY/jodi_digit.html')

def MILANDAYSINGLEPANA(request):
    return render (request,'MILANDAY/singlepanna.html')

def MILANDAYDOUBLEPANA(request):
    return render (request,'MILANDAY/doublepanna.html')

def MILANDAYTRIPLEPANA(request):
    return render (request,'MILANDAY/triplepanna.html')

def MILANDAYHALFSANGAM(request):
    return render (request,'MILANDAY/halfsangam.html')

def MILANDAYFULLSANGAM(request):
    return render (request,'MILANDAY/fullsangam.html')
# MILANDAY END
# RAJDHANI DAY
def RAJDHANIDAY(request):
    return render (request,'RAJDHANIDAY/rajdhaniday.html')

def RAJDHANIDAYSINGLEDIGIT(request):
    return render (request,'RAJDHANIDAY/single_digit.html')

def RAJDHANIDAYJODIDIGIT(request):
    return render (request,'RAJDHANIDAY/jodi_digit.html')

def RAJDHANIDAYJSINGLEPANA(request):
    return render (request,'RAJDHANIDAY/singlepanna.html')

def RAJDHANIDAYDOUBLEPANA(request):
    return render (request,'RAJDHANIDAY/doublepanna.html')

def RAJDHANIDAYTRIPLEPANA(request):
    return render (request,'RAJDHANIDAY/triplepanna.html')

def RAJDHANIDAYHALFSANGAM(request):
    return render (request,'RAJDHANIDAY/halfsangam.html')

def RAJDHANIDAYFULLSANGAM(request):
    return render (request,'RAJDHANIDAY/fullsangam.html')
# RAJDHANI DAY END
# SUPREME DAY START
def SUPREMEDAY(request):
    return render (request,'SUPREMEDAY/supremeday.html')

def SUPREMEDAYSINGLEDIGIT(request):
    return render (request,'SUPREMEDAY/single_digit.html')

def SUPREMEDAYJODIDIGIT(request):
    return render (request,'SUPREMEDAY/jodi_digit.html')

def SUPREMEDAYSINGLEPANA(request):
    return render (request,'SUPREMEDAY/singlepanna.html')

def SUPREMEDAYDOUBLEPANA(request):
    return render (request,'SUPREMEDAY/doublepanna.html')

def SUPREMEDAYTRIPLEPANA(request):
    return render (request,'SUPREMEDAY/triplepanna.html')

def SUPREMEDAYHALFSANGAM(request):
    return render (request,'SUPREMEDAY/halfsangam.html')

def SUPREMEDAYFULLSANGAM(request):
    return render (request,'SUPREMEDAY/fullsangam.html')
# SUPREME DAY END
# KALYAN START
def KALYAN(request):
    return render (request,'KALYAN/kalyan.html')

def KALYANSINGLEDIGIT(request):
    return render (request,'KALYAN/single_digit.html')

def KALYANJODIDIGIT(request):
    return render (request,'KALYAN/jodi_digit.html')

def KALYANSINGLEPANA(request):
    return render (request,'KALYAN/singlepanna.html')

def KALYANDOUBLEPANA(request):
    return render (request,'KALYAN/doublepanna.html')

def KALYANTRIPLEPANA(request):
    return render (request,'KALYAN/triplepanna.html')

def KALYANHALFSANGAM(request):
    return render (request,'KALYAN/halfsangam.html')

def KALYANFULLSANGAM(request):
    return render (request,'KALYAN/fullsangam.html')
# KALYAN END

# SRIDEVI NIGHT START
def SRIDEVINIGHT(request):
    return render (request,'SRIDEVINIGHT/sridevinight.html')

def SRIDEVINIGHTSINGLEDIGIT(request):
    return render (request,'SRIDEVINIGHT/single_digit.html')

def SRIDEVINIGHTJODIDIGIT(request):
    return render (request,'SRIDEVINIGHT/jodi_digit.html')

def SRIDEVINIGHTSINGLEPAMNA(request):
    return render (request,'SRIDEVINIGHT/singlepanna.html')

def SRIDEVINIGHTDOUBLEPANA(request):
    return render (request,'SRIDEVINIGHT/doublepanna.html')

def SRIDEVINIGHTTRIPLEPANA(request):
    return render (request,'SRIDEVINIGHT/triplepanna.html')

def SRIDEVINIGHTHALFSANGAM(request):
    return render (request,'SRIDEVINIGHT/halfsangam.html')

def SRIDEVINIGHTFULLSANGAM(request):
    return render (request,'SRIDEVINIGHT/fullsangam.html')
# SRIDEVI NIGHT END
# MADHUR NIGHT START
def MADHURINIGHT(request):
    return render (request,'MADHURNIGHT/madhurnight.html')

def MADHURNIGHTSINGLEDIGIT(request):
    return render (request,'MADHURNIGHT/single_digit.html')

def MADHURNIGHTJODIDIGIT(request):
    return render (request,'MADHURNIGHT/jodi_digit.html')

def MADHURNIGHTSINGLEPANA(request):
    return render (request,'MADHURNIGHT/singlepanna.html')

def MADHURNIGHTDOUBLEPANA(request):
    return render (request,'MADHURNIGHT/doublepanna.html')

def MADHURNIGHTTRIPLEPANA(request):
    return render (request,'MADHURNIGHT/triplepanna.html')

def MADHURNIGHTHALFSANGAM(request):
    return render (request,'MADHURNIGHT/halfsangam.html')

def MADHURNIGHTFULLSANGAM(request):
    return render (request,'MADHURNIGHT/fullsangam.html')
# MADHRU NIGHT END
# NEW MUMBAI START
def NEWMAINMUMBAI(request):
    return render (request,'NEWMAINMUMBAI/newmainmumbai.html')

def NEWMAINMUMBAISINGLEDIGIT(request):
    return render (request,'NEWMAINMUMBAI/single_digit.html')

def NEWMAINMUMBAIJODIDIGIT(request):
    return render (request,'NEWMAINMUMBAI/jodi_digit.html')

def NEWMAINMUMBAISINGLEPANA(request):
    return render (request,'NEWMAINMUMBAI/singlepanna.html')

def NEWMAINMUMBAIDOUBLEPANA(request):
    return render (request,'NEWMAINMUMBAI/doublepanna.html')

def NEWMAINMUMBAITRIPLEPANA(request):
    return render (request,'NEWMAINMUMBAI/triplepanna.html')

def NEWMAINMUMBAIHALFSANGAM(request):
    return render (request,'NEWMAINMUMBAI/halfsangam.html')

def NEWMAINMUMBAIFULLSANGAM(request):
    return render (request,'NEWMAINMUMBAI/fullsangam.html')
# NEW MAIN MUMBAI END
# SUPREME NIGHT START
def SUPREMENIGHT(request):
    return render (request,'SUPREMENIGHT/supremenight.html')

def SUPREMENIGHTSINGLEDIGIT(request):
    return render (request,'SUPREMENIGHT/single_digit.html')

def SUPREMENIGHTJODIDIGIT(request):
    return render (request,'SUPREMENIGHT/jodi_digit.html')

def SUPREMENIGHTSINGLEPANA(request):
    return render (request,'SUPREMENIGHT/singlepanna.html')

def SUPREMENIGHTDOUBLEPANA(request):
    return render (request,'SUPREMENIGHT/doublepanna.html')

def SUPREMENIGHTTRIPLEPANA(request):
    return render (request,'SUPREMENIGHT/triplepanna.html')

def SUPREMENIGHTHALFSANGAM(request):
    return render (request,'SUPREMENIGHT/halfsangam.html')

def SUPREMENIGHTFULLSANGAM(request):
    return render (request,'SUPREMENIGHT/fullsangam.html')
# SUPREME NIGHT END
# MILAN NIGHT START
def MILANNIGHT(request):
    return render (request,'MILANNIGHT/milannight.html')

def MILANNIGHTSINGLEDIGIT(request):
    return render (request,'MILANNIGHT/single_digit.html')

def MILANNIGHTJODIDIGIT(request):
    return render (request,'MILANNIGHT/jodi_digit.html')

def MILANNIGHTSINGLEPANA(request):
    return render (request,'MILANNIGHT/singlepanna.html')

def MILANNIGHTDOUBLEPANA(request):
    return render (request,'MILANNIGHT/doublepanna.html')

def MILANNIGHTJTRIPLEPANA(request):
    return render (request,'MILANNIGHT/triplepanna.html')

def MILANNIGHTHALFSANGAM(request):
    return render (request,'MILANNIGHT/halfsangam.html')

def MILANNIGHTFULLSANGAM(request):
    return render (request,'MILANNIGHT/fullsangam.html')
# MILAN NIGHT END
# KALYAN NIGHT START
def KALYANNIGHT(request):
    return render (request,'KALYANNIGHT/kalyannight.html')

def KALYANNIGHTSINGLEDIGIT(request):
    return render (request,'KALYANNIGHT/single_digit.html')

def KALYANNIGHTJODIDIGIT(request):
    return render (request,'KALYANNIGHT/jodi_digit.html')

def KALYANNIGHTSINGLEPANA(request):
    return render (request,'KALYANNIGHT/singlepanna.html')

def KALYANNIGHTDOUBLEPANA(request):
    return render (request,'KALYANNIGHT/doublepanna.html')

def KALYANNIGHTTRIPLEPANA(request):
    return render (request,'KALYANNIGHT/triplepanna.html')

def KALYANNIGHTHALFSANGAM(request):
    return render (request,'KALYANNIGHT/halfsangam.html')

def KALYANNIGHTFULLSANGAM(request):
    return render (request,'KALYANNIGHT/fullsangam.html')
# KALYAN NIGHT END
# RAJDHANI NIGHT START
def RAJDHANINIGHT(request):
    return render (request,'RAJADHANINIGHT/rajadhaninight.html')

def RAJDHANINIGHTSINGLEDIGIT(request):
    return render (request,'RAJADHANINIGHT/single_digit.html')

def RAJDHANINIGHTJODIDIGIT(request):
    return render (request,'RAJADHANINIGHT/jodi_digit.html')

def RAJDHANINIGHTSINGLEPANA(request):
    return render (request,'RAJADHANINIGHT/singlepanna.html')

def RAJDHANINIGHTDOUBLEPANA(request):
    return render (request,'RAJADHANINIGHT/doublepanna.html')

def RAJDHANINIGHTTRIPLEPANA(request):
    return render (request,'RAJADHANINIGHT/triplepanna.html')

def RAJDHANINIGHTHALFSANGAM(request):
    return render (request,'RAJADHANINIGHT/halfsangam.html')

def RAJDHANINIGHTFULLSANGAM(request):
    return render (request,'RAJADHANINIGHT/fullsangam.html')
# RAJDHANI NIGHT START
# MAIN BAZAR START
def MAINBAZAR(request):
    return render (request,'MAINBAZAR/mainbazar.html')

def MAINBAZARSINGLEDIGIT(request):
    return render (request,'MAINBAZAR/single_digit.html')

def MAINBAZARJODIDIGIT(request):
    return render (request,'MAINBAZAR/jodi_digit.html')

def MAINBAZARSINGLEPANA(request):
    return render (request,'MAINBAZAR/singlepanna.html')

def MAINBAZARDOUBLEPANA(request):
    return render (request,'MAINBAZAR/doublepanna.html')

def MAINBAZARTRIPLEPANA(request):
    return render (request,'MAINBAZAR/triplepanna.html')

def MAINBAZARHALFSANGAM(request):
    return render (request,'MAINBAZAR/halfsangam.html')

def MAINBAZARFULLSANGAM(request):
    return render (request,'MAINBAZAR/fullsangam.html')
# MAIN BAZAR END
# STARLINE TIME 
def TENAM(request):
    return render (request,'STARLINE/10am.html')
def ELEVENAM(request):
    return render (request,'STARLINE/11am.html')
def TWELEPM(request):
    return render (request,'STARLINE/12pm.html')
def ONEPM(request):
    return render (request,'STARLINE/01pm.html')
def TWOPM(request):
    return render (request,'STARLINE/02pm.html')
def THREEPM(request):
    return render (request,'STARLINE/03pm.html')
def FOURPM(request):
    return render (request,'STARLINE/04pm.html')
def FIVEPM(request):
    return render (request,'STARLINE/05pm.html')
def SIXPM(request):
    return render (request,'STARLINE/06pm.html')
def SEVEANPM(request):
    return render (request,'STARLINE/07pm.html')
def EIGHTPM(request):
    return render (request,'STARLINE/08pm.html')
def NINEPM(request):
    return render (request,'STARLINE/09pm.html')
def TENPM(request):
    return render (request,'STARLINE/10pm.html')
# STARLINE TIME END
# 10:00 AM START
def TENAMSINGLEDIGIT(request):
    return render (request,'10AM/singledigit.html')
def TENAMSINGLEPANA(request):
    return render (request,'10AM/singlepana.html')
def TENAMDOUBLEPANA(request):
    return render (request,'10AM/doublepana.html')
def TENAMTRIPLEPANA(request):
    return render (request,'10AM/triplepana.html')
# 11AM START
def ELEVENAMSINGLEDIGIT(request):
    return render (request,'11AM/singledigit.html')
def ELEVENAMSINGLEPANA(request):
    return render (request,'11AM/singlepana.html')
def ELEVENAMDOUBLEPANA(request):
    return render (request,'11AM/doublepana.html')
def ELEVENAMTRIPLEPANA(request):
    return render (request,'11AM/triplepana.html')
# 12PM
def TWELEPMSINGLEDIGIT(request):
    return render (request,'12PM/singledigit.html')

def TWELEPMSINGLEPANA(request):
    return render (request,'12PM/singlepana.html')

def TWELEPMDOUBLEPANA(request):
    return render (request,'12PM/doublepana.html')

def TWELEPMTRIPLEPANA(request):
    return render (request,'12PM/triplepana.html')
# 01PM
def ONEPMSINGLEDIGIT(request):
    return render (request,'01PM/singledigit.html')

def ONEPMSINGLEPANA(request):
    return render (request,'01PM/singlepana.html')

def ONEPMDOUBLEPANA(request):
    return render (request,'01PM/doublepana.html')

def ONEPMTRIPLEPANA(request):
    return render (request,'01PM/triplepana.html')
# 02PM
def TWOPMSINGLEDIGIT(request):
    return render (request,'02PM/singledigit.html')

def TWOPMSINGLEPANA(request):
    return render (request,'02PM/singlepana.html')

def TWOPMDOUBLEPANA(request):
    return render (request,'02PM/doublepana.html')

def TWOPMTRIPLEPANA(request):
    return render (request,'02PM/triplepana.html')
# 03PM
def THREEPMSINGLEDIGIT(request):
    return render (request,'03PM/singledigit.html')

def THREEPMSINGLEPANA(request):
    return render (request,'03PM/singlepana.html')

def THREEPMDOUBLEPANA(request):
    return render (request,'03PM/doublepana.html')

def THREEPMTRIPLEPANA(request):
    return render (request,'03PM/triplepana.html')
# 04PM
def FOURPMSINGLEDIGIT(request):
    return render (request,'04PM/singledigit.html')

def FOURPMSINGLEPANA(request):
    return render (request,'04PM/singlepana.html')

def FOURPMDOUBLEPANA(request):
    return render (request,'04PM/doublepana.html')

def FOURPMTRIPLEPANA(request):
    return render (request,'04PM/triplepana.html')
# 05 PM
def FIVEPMSINGLEDIGIT(request):
    return render (request,'05PM/singledigit.html')

def FIVEPMSINGLEPANA(request):
    return render (request,'05PM/singlepana.html')

def FIVEPMDOUBLEPANA(request):
    return render (request,'05PM/doublepana.html')

def FIVEPMTRIPLEPANA(request):
    return render (request,'05PM/triplepana.html')
# 06PM
def SIXPMSINGLEDIGIT(request):
    return render (request,'06PM/singledigit.html')

def SIXPMSINGLEPANA(request):
    return render (request,'06PM/singlepana.html')

def SIXPMDOUBLEPANA(request):
    return render (request,'06PM/doublepana.html')

def SIXPMTRIPLEPANA(request):
    return render (request,'06PM/triplepana.html')
# 07PM
def SEVENPMSINGLEDIGIT(request):
    return render (request,'07PM/singledigit.html')

def SEVENPMSINGLEPANA(request):
    return render (request,'07PM/singlepana.html')

def SEVENPMDOUBLEPANA(request):
    return render (request,'07PM/doublepana.html')

def SEVENPMTRIPLEPANA(request):
    return render (request,'07PM/triplepana.html')
# 08PM
def EIGHTPMSINGLEDIGIT(request):
    return render (request,'08PM/singledigit.html')

def EIGHTPMSINGLEPANA(request):
    return render (request,'08PM/singlepana.html')

def EIGHTPMDOUBLEPANA(request):
    return render (request,'08PM/doublepana.html')

def EIGHTPMTRIPLEPANA(request):
    return render (request,'08PM/triplepana.html')
# 09PM
def NINEPMSINGLEDIGIT(request):
    return render (request,'09PM/singledigit.html')

def NINEPMSINGLEPANA(request):
    return render (request,'09PM/singlepana.html')

def NINEPMDOUBLEPANA(request):
    return render (request,'09PM/doublepana.html')

def NINEPMTRIPLEPANA(request):
    return render (request,'09PM/triplepana.html')
# 10PM
def TENPMSINGLEDIGIT(request):
    return render (request,'10PM/singledigit.html')

def TENPMSINGLEPANA(request):
    return render (request,'10PM/singlepana.html')

def TENPMDOUBLEPANA(request):
    return render (request,'10PM/doublepana.html')

def TENPMTRIPLEPANA(request):
    return render (request,'10PM/triplepana.html')
# GALIDISAWAR
def DISAWAR(request):
    return render (request,'Galidisawar/disawar.html')

def FARIDABAAD(request):
    return render (request,'Galidisawar/faridabaad.html')

def GAZIABAAD(request):
    return render (request,'Galidisawar/gaziabaad.html')

def GALI(request):
    return render (request,'Galidisawar/gali.html')


