# Gerador de Senhas

Este é um projeto simples que gera senhas aleatórias com base nas propriedades selecionadas pelo usuário. A interface WEB é um simples formulário HTML que juntamente com o Flask usa o app.py para gerar a senha.

O código utiliza o módulo `random` do Python para gerar senhas aleatórias. O usuário pode selecionar as propriedades das quais deseja que a senha seja composta, como números, letras maiúsculas, letras minúsculas, caracteres especiais e o tamanho da senha.

## Tecnologias Utilizadas

- Python
- Flask

### Atenção!

1. Certifique-se de ter o Python instalado em seu sistema.
2. Faça o download ou clone este repositório em sua máquina local.

## Instalação & Inicio Automático

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/rodolfoluizbr/gerador_de_senha_flask.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd gerador_de_senha_flask
   ```
   
3. Rode o código start.py

   ```bash
   python3 start.py
   ```


## Instalação & Inicio Manual

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/rodolfoluizbr/gerador_de_senha_flask.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd gerador_de_senha_flask
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências do projeto:

   ```bash
   pip install flask
   ```


5. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

6. Abra o navegador e acesse o endereço `http://localhost:5000`.

7. Preencha os campos do formulário e clique no botão "Gerar Senha".

8. A senha gerada será exibida na página.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
