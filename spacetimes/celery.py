from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from django.apps import apps

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spacetimes.settings')

app = Celery('spacetimes',broker='redis://localhost:6379')

app.config_from_object(settings)
app.conf.enable_utc = True
app.Task.track_started = True
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

