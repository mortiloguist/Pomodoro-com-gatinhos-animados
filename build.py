import PyInstaller.__main__
import os

# Obtém o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Configuração do PyInstaller
PyInstaller.__main__.run([
    'pomodoro.py',  # Arquivo principal
    '--onefile',    # Cria um único arquivo executável
    '--name=PomodoroGatinhos',  # Nome do executável
    '--noconsole',  # Não mostra a janela do console
    '--icon=icon.ico',  # Ícone do programa (opcional)
    '--add-data=requirements.txt;.',  # Inclui arquivos adicionais
    '--clean',      # Limpa arquivos temporários
    '--windowed',   # Modo janela
]) 