from celery_main import app
@app.task
def hello2(nome):
    print(nome+' task2')
