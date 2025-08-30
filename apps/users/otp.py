from django.core.cache import cache
from django.conf import settings
import random
import time
import hashlib
import hmac



def genarator_OTP (phone_number):
 
    key_otp = f'otp_code_{phone_number}'            # ساهتن یه کلید برای اینکه بتونیم بشناسیمش
    generate_otp = random.randint(100000 , 999999)
    
    signature = hmac.HMAC(                        #ساهتن یه امضای درست برای این 
        key= settings.SECRET_KEY.encode() ,
        msg = str(generate_otp).encode(),
        digestmod = hashlib.sha256,
    ).hexdigest()

    old_Data = cache.get(key_otp)

    if old_Data :
        tekrar = old_Data['tekrar'] +1
        cache.set(key_otp ,cache_data , 180 )

    else:
        tekrar = 1

    cache_data = {'signature':signature , 'time':time.time()+180  , 'tekrar': tekrar }        # ساختن یه اطلاعات داده برای اینکه کلا set بشه

    cache.set(key_otp ,cache_data , 180 )

    
    
    return  generate_otp , True , cache_data['time'] ,cache_data['tekrar'] , signature
    
  
   
    

def validator_OTP (phon_number , OTP ):
    if phon_number is None :
        return  False , 'شماره تلفن وجود ندارد'
    key_otp = f'otp_code_{phon_number}'
    otp_code = cache.get(key_otp)

    signature = hmac.HMAC(
        key = settings.SECRET_KEY.encode(),
        msg = str(OTP).encode(),
        digestmod = hashlib.sha256,
    ).hexdigest()


    if hmac.compare_digest(signature , otp_code['signature']):
        otp_code['tekrar']+1
        return True , 'خوش امدید'
    else:
        return False , 'کد اشتباه وارد کردید'
        
   
    

def delete_OTP (phone_number):
    key_otp =  f'otp_code_{phone_number}'
    cache.delete(key_otp)





