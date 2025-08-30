from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from apps.users.models import CustomUser



phon_number_iran = RegexValidator(
    regex=r'^(\+98|0)?9\d{9}$', 
    message='شماره موبایل معتبر وارد کنید'
)


class create_user_phone_FORM (forms.Form):

    phone_number = forms.CharField(max_length=11 , validators=[phon_number_iran] , label='شماره تلفن')

class otp_uaer_FORM (forms.Form):

    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder' : 'کد 6 رقمی وارد کنید'}))

class userName_FORM (forms.ModelForm):
    username = forms.CharField(max_length=20 ,)
    class Meta:
        model = CustomUser
        fields = ['username']
        
class loginAndSign(UserCreationForm):
    class Meta :
        model = CustomUser
        fields = ['phone_number','password1','password2']

