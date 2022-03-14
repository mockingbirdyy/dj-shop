from celery import shared_task
from datetime import datetime, timedelta
from accounts.models import OtpCode
import pytz


@shared_task
def remove_expired_otp_codes():
    expire_time = datetime.now(tz=pytz.timezone("Asia/Tehran")) - timedelta(minutes=1)
    OtpCode.objects.filter(created_lt=expire_time).delete()
