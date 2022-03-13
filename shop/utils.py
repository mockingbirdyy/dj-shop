from random import randint  
from accounts.models import OtpCode
from kavenegar import *
# creating a one time pass code and send it for user  
def send_otp_code(phone_number):
    random_code = randint(1000, 9999)
    OtpCode.objects.create(phone_number=phone_number, code=random_code)
    '''sending code to user using sms service, here using kavenegar.
       installing kavenegar: <pip install kavenegar> '''
  
    try:
        # creating an instance from kavenegar giving your own APIKEY as arg,
        # set params and send it 
        api = KavenegarAPI('Your APIKEY')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'Your verification code is: {code}',
        }
        response = api.sms_send(params=params)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)

#############################################################################
