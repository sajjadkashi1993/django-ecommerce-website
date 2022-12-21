from core.sms import SmsAPI, APIException, HTTPException
from API_keys import SMS_API_KEY


def send_otp_code(phone: str, otp_code: str):
    try:
        api = SmsAPI(SMS_API_KEY)
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
        print(str(response))
    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(str(e))
