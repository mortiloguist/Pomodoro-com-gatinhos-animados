import PyInstaller.__main__

# Configuração do PyInstaller
PyInstaller.__main__.run([
    'pomodoro.py',  # Arquivo principal
    '--onefile',    # Cria um único arquivo executável
    '--name=PomodoroGatinhos',  # Nome do executável
    '--clean',      # Limpa arquivos temporários
]) 