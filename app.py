from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('formulario.html')  # Renderiza o template 'formulario.html' ao acessar a rota principal '/'

@app.route('/gerar_senha', methods=['POST'])
def gerar_senha():
    n = "1234567890"  # Dígitos numéricos
    mi = "abcdefghijklmnopqrstuvwxyz"  # Letras minúsculas
    ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letras maiúsculas
    e = "%$#-_&"  # Caracteres especiais
    all = n * 8 + mi * 8 + ma * 8 + e * 8  # Todas as opções

    seleciona = request.form.getlist('propriedades')  # Obtém as opções selecionadas pelo formulário

    prefixo = request.form['prefixo']  # Obtém o valor do campo 'prefixo' enviado pelo formulário
    sufixo = request.form['sufixo']  # Obtém o valor do campo 'sufixo' enviado pelo formulário
    tamanho = int(request.form['tamanho'])  # Obtém o valor do campo 'tamanho' enviado pelo formulário convertido para inteiro

    selecionadas = []
    for opcao in seleciona:
        if opcao == "all":
            selecionadas.append(all)  # Adiciona a string 'all' à lista 'selecionadas'
        elif opcao == "ma":
            selecionadas.append(ma)  # Adiciona a string 'ma' à lista 'selecionadas'
        elif opcao == "mi":
            selecionadas.append(mi)  # Adiciona a string 'mi' à lista 'selecionadas'
        elif opcao == "n":
            selecionadas.append(n)  # Adiciona a string 'n' à lista 'selecionadas'
        elif opcao == "e":
            selecionadas.append(e)  # Adiciona a string 'e' à lista 'selecionadas'

    seleciona = "".join(selecionadas)  # Junta as strings da lista 'selecionadas' em uma única string

    senha = prefixo + "".join(random.sample(seleciona, tamanho)) + sufixo  # Gera a senha a partir das opções selecionadas, prefixo, sufixo e tamanho

    return render_template('formulario.html', senha=senha)  # Renderiza o template 'formulario.html' e passa a senha gerada para ser exibida

if __name__ == '__main__':
    app.run()  # Inicia o servidor Flask
