import os
import subprocess
import sys
import webbrowser

# Verifica se o ambiente virtual já está configurado
if not os.path.exists('venv'):
    # Cria um ambiente virtual
    subprocess.call([sys.executable, '-m', 'venv', 'venv'])

# Ativa o ambiente virtual
activate_script = os.path.join('venv', 'Scripts', 'activate')
subprocess.call(activate_script, shell=True)

# Instala as dependências do Flask
subprocess.call(['pip', 'install', 'flask'])

# Executa o aplicativo Flask
subprocess.Popen([sys.executable, 'app.py'])

# Aguarda alguns segundos para que o servidor Flask seja iniciado
# Você pode ajustar o tempo de espera conforme necessário
import time
time.sleep(10)

# Abre o servidor local no navegador padrão do sistema
webbrowser.open('http://localhost:5000')
