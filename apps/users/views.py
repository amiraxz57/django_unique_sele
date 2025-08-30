from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from apps.users.models import CustomUser
from apps.users.forms import otp_uaer_FORM , CustomUser , create_user_phone_FORM , loginAndSign ,userName_FORM
from apps.users.otp import delete_OTP , genarator_OTP , validator_OTP
import time
# Create your views here.

def resive_phone_OTP_VIEWS (request):

    if request.method == 'POST':
        form = create_user_phone_FORM(request.POST)
       
        if form.is_valid():
            phone = form.cleaned_data['phone_number']  # گرفتن شماره یه شکل درست 
            request.session['phone'] = phone
             
            delete_OTP(phone)
            otp , seccsec , time_OTP , TEKRAR , signature = genarator_OTP(phone)            #ساخت یه نوع کد و جک کردن اینکه کد ساهته شده یا نه 

            if TEKRAR < 3 :                                                    # اگر بیش از حد تکرار داشت 

                if time_OTP >= time.time():          
                                                # اگر تایمش گدشت
                    if seccsec :

                        messages.success(request , 'کد با موفقیت ارسال شد ')
                        print(otp)
                        print(time_OTP)
                        print(TEKRAR)
                        print(signature)
                        return redirect('users:otp')

                    else:
                        messages(request , 'کد ارسال نشده یا شماره اشتباه است')
                        return redirect('users:login')
                else:
                    messages.error(request , 'تایم درخواست شما منضصی شده است')
            else:
                messages.error(request , 'شما بیش از حد درخواست کد کردید به مدت 5 ساعت بعد درخواست بفرمایید')
            
    else:
        form = create_user_phone_FORM()
    
    return render (request , 'users/login.html' , {'form':form})


def validate_otp_VIEW (request):

    if request.method == 'POST':
        phone_number = request.session['phone']
        form = otp_uaer_FORM(request.POST)

        print(phone_number)
       
        if form.is_valid():
            OTP_USER = form.cleaned_data['otp']
            valid =validator_OTP( phone_number ,OTP_USER )
           

            if valid:
                User = CustomUser.objects.create_user(phone_number = phone_number )
                login(request , User , backend = 'users.CustomUser')

                return redirect('users:profile')
            else :
                messages.error(request , 'کد وارد شده معتبر نیست ')
    
    else:
        form = otp_uaer_FORM()

    return render(request , 'users/otp.html' , {'form':form})


            


    


