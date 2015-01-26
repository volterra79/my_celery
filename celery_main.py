from __future__ import absolute_import
from celery import Celery

app=Celery(broker='redis://localhost:6379/0', include=['celery_tasks.group1.tasks'])
