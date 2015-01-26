from __future__ import absolute_import
from celery import Celery

#app=Celery(broker='redis://localhost:6379/0', include=['tasks.tasks'])
app=Celery('tasks.tasks',broker='redis://localhost:6379/0')

#app.send_task('package.nodulo.function',(arg1,arg2,))