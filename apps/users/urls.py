from django.urls import path 
from apps.users.views import  validate_otp_VIEW , resive_phone_OTP_VIEWS

app_name = 'users'

urlpatterns = [
    path('' , resive_phone_OTP_VIEWS , name = 'resive_phone' ),
    path('otpvalid/' , validate_otp_VIEW , name = 'otp' ),

]
