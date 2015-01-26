from client_env.c_main import app
print('Passo da modulo')
@app.task
def ciao(nome):
    print('Hello '+nome)
