from flask import Flask, render_template, request # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<entrada>')
def validaCPF(entrada):

#    digitaCPF = request.args.get('cpf')
    
#    entrada = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    cpf_lista ='blacklist.txt'
    cpf_valido = False
    
    with open(cpf_lista ,'r') as c:
        linha = 1
        for cpf in c:
            if entrada == cpf.strip():
                cpf_valido = True
                break
            else:
                cpf_valido = False
            linha+=1
    c.close()

    if cpf_valido:
        return 'Block'
    else:
        return 'Livre' 
    

if __name__ == '__main__':
    app.run() # Executa a aplicação