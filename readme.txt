# 🐱 Pomodoro Timer com Gatinhos Animados 🐱

Um timer Pomodoro interativo no terminal com dois gatinhos animados (Luna e Artemis) para te acompanhar durante suas sessões de estudo/trabalho!

## ✨ Características

- ⏰ Timer Pomodoro padrão (25min trabalho, 5min pausa curta, 20min pausa longa)
- 🐱 Dois gatinhos animados com expressões diferentes
- 🎨 Interface colorida e amigável no terminal
- 📊 Controle de sessões e modos
- 🎵 Notificações sonoras (em desenvolvimento)

## 🚀 Como Usar

### Requisitos
- Python 3.10 ou superior (apenas para desenvolvimento)
- Terminal com suporte a caracteres Unicode
- Tamanho mínimo da janela: 80x20 caracteres

### Controles

- `Espaço`: Iniciar/Pausar o timer
- `n`: Pular para a próxima fase
- `s`: Parar a sessão atual
- `q`: Sair do programa

## 🐱 Os Gatinhos

### Luna (Esquerda)
- Expressões: (o.o), (-.-), (^.^)
- Personalidade: Calma e observadora
- Posição: Lado esquerdo do timer

### Artemis (Direita)
- Expressões: (>.o), (-.-), (^.^)
- Personalidade: Mais ativa e curiosa
- Posição: Lado direito do timer

## ⚙️ Configuração

Os tempos padrão são:
- Trabalho: 25 minutos
- Pausa curta: 5 minutos
- Pausa longa: 20 minutos
- Sessões antes da pausa longa: 4

## 🛠️ Desenvolvimento

### Estrutura do Projeto
```
pomodoro-gatinhos/
├── pomodoro.py      # Código principal
├── build.py         # Script para criar executável
├── requirements.txt # Dependências
└── readme.txt      # Este arquivo
```

### Tecnologias Utilizadas
- Python 3.10+
- Biblioteca curses para interface no terminal
- Caracteres Unicode para animações
- PyInstaller para criar executável

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com o projeto! Algumas ideias:
- Adicionar mais animações
- Implementar notificações sonoras
- Criar temas diferentes
- Adicionar estatísticas de uso

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- Inspirado na técnica Pomodoro
- Nomes dos gatinhos inspirados em Sailor Moon 🌙
