from flask_mail import Mail
from celery import Celery

mail = Mail()

celery = Celery(__name__)
