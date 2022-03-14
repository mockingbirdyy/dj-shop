from django.core.management import BaseCommand
from datetime import datetime, timedelta
from accounts.models import OtpCode
import pytz



class Command(BaseCommand):
    help = 'removes all expired OtpCodes in db'

    def handle(self, *args, **options):
        expire_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expire_time).delete()
        self.stdout.write('all expired OtpCodes deleted')