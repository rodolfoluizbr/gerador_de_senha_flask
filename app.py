from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/gerar_senha', methods=['POST'])
def gerar_senha():
    n = "1234567890"
    mi = "abcdefghijklmnopqrstuvwxyz"
    ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    e = "%$#-_&"
    all = n * 8 + mi * 8 + ma * 8 + e * 8

    seleciona = request.form.getlist('propriedades')

    prefixo = request.form['prefixo']
    sufixo = request.form['sufixo']
    tamanho = int(request.form['tamanho'])

    selecionadas = []
    for opcao in seleciona:
        if opcao == "all":
            selecionadas.append(all)
        elif opcao == "ma":
            selecionadas.append(ma)
        elif opcao == "mi":
            selecionadas.append(mi)
        elif opcao == "n":
            selecionadas.append(n)
        elif opcao == "e":
            selecionadas.append(e)

    seleciona = "".join(selecionadas)

    senha = prefixo + "".join(random.sample(seleciona, tamanho)) + sufixo

    return render_template('formulario.html', senha=senha)

if __name__ == '__main__':
    app.run()
