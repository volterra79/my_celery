from __future__ import absolute_import
from celery import Celery
app=Celery('w_main', broker='redis://localhost:6379/0')
#app=Celery(broker='redis://localhost:6379/0', include=['tasks.tasks'])
@app.task
def ciao(nome):
    print('Internal name '+nome)
