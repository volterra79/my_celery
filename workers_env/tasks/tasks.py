import sys
sys.path.append('/var/www/CELERY_TEST')
from workers_env.w_main import app
@app.task
def ciao(nome):
    print('Hallo '+nome)

