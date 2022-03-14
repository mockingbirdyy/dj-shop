from celery import Celery
import os
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
celery_app = Celery('shop')

celery_app.autodiscover_tasks()

# celery configs
celery_app.conf.broker_url = 'amqp://'
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'json'
celery_app.conf.accept_content = ['json']
celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 4

