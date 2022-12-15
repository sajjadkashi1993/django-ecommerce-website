from core.sms import SmsAPI, APIException, HTTPException
from django.conf import settings


def send_otp_code(phone: str, otp_code: str):
    try:
        api = SmsAPI(settings.SMS_API_KEY)
        params = {
            "mobile": phone,
            "templateId": 100000,
            "parameters": [
                {
                    "name": "code",
                    "value": otp_code
                }

            ]
        }
        response = api.sms_verify_send(params)
        print(12222222222222222222222222222)
        print(str(response))
    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(str(e))
