from flask import Flask, render_template, request # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<cpf>')
def validaCPF(cpf):

    entrada = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]) #Faz um tratamento do CPF 
    cpf_lista ='blacklist.txt' # Arquivo de Black list dos CPF
    cpf_valido = False
    
    with open(cpf_lista ,'r') as c: # Validação da Regra
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