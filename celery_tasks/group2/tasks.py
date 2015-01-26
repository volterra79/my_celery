from celery_main import app
@app.task
def hello1(nome):
    print(nome)
