from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_configurations.settings")   # {NOTE: 2nd parameter is our django_project_name.settings}

app = Celery("celery_configurations")    # write django project name here
app.conf.enable_utc = False

app.conf.update(timezone="Aisa/Kolkata")

app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_scheduler = {

}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request}")

