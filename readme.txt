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
- Python 3.10 ou superior
- Terminal com suporte a caracteres Unicode
- Tamanho mínimo da janela: 80x20 caracteres

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/pomodoro-gatinhos.git
cd pomodoro-gatinhos
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando

```bash
python pomodoro.py
```

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
├── requirements.txt # Dependências
└── readme.txt      # Este arquivo
```

### Tecnologias Utilizadas
- Python 3.10+
- Biblioteca curses para interface no terminal
- Caracteres Unicode para animações

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

Terminal Pomodoro Timer com Gestão de Sessões

Objetivo:
Criar um programa de terminal interativo que implemente a técnica Pomodoro com gestão completa de sessões, histórico e personalização.

Requisitos Técnicos:

Linguagem: Python 3.10+

Dependências:

time (nativa)

curses (para interface)

platform (para notificações multiplataforma)

json (histórico)

argparse (CLI)

Funcionalidades Principais:

1. Ciclo Pomodoro Padrão:

25min trabalho → 5min pausa curta (×4) → 20min pausa longa

Exibir relógio circular ASCII animado com:

╭────────────╮
│  ◯ 25:00  │ 
│  \|||||/  │
╰────────────╯
Atualização a cada segundo com diferentes animações de progresso

2. Controles Interativos (teclas):

Space: Iniciar/Pausar

s: Parar sessão

n: Pular fase

c: Personalizar tempos

h: Ver histórico

q: Sair com confirmação

3. Sistema de Notificações:

Alertas multiplataforma:

Linux: notify-send

macOS: osascript -e 'display notification'

Windows: winsound.Beep

Mensagens sonoras opcionais (configurável)

4. Personalização:

Argumentos CLI:

bash
pomodoro --work 30 --short-break 7 --long-break 25 --sessions 8
Menu de configuração em tempo real (curses)

5. Estatísticas e Histórico:

Registro em JSON:

json
{
  "date": "2024-02-20",
  "sessions": [
    {"type": "work", "duration": 25, "completed": true},
    {"type": "break", "duration": 5, "completed": false}
  ]
}
Relatório diário/semanal (gráficos ASCII)

6. Modos Especiais:

Modo foco total (esconde interface)

Modo desafio (acumula tempo produtivo)

Modo colaborativo (sincronização via socket)

Fluxograma:

Inicialização → Carregar configurações

Loop principal → Atualizar UI

Gerenciador de eventos → Processar teclas

Temporizador → Notificações/Atualizações

Encerramento → Salvar histórico

Testes Necessários:

Validação de entrada de tempo (1-60min)

Recuperação de sessão interrompida

Compatibilidade cross-platform

Gestão de zona horária para histórico

Entregáveis:

Script executável pomodoro.py

Arquivo de configuração ~/.pomodororc

Documentação em README.md (instalação/uso)

Pacote PyPI opcional

Exemplo de UI:

[POMODORO] 14:32 ⏰ | Trabalho #3 (2/4 concluídos)
──────────────────────────────────────
Tempo Restante:   12:45 
Progresso:        █████████░░░░ 65%
Próxima Pausa:    Longa (20:00)

Comandos: [Space] ⏯️ | [s] ⏹️ | [n] ⏭️ | [q] 🚪

Requisitos Não Funcionais:

Baixo consumo de CPU (<2% em idle)

Suporte a temas/cor personalizados

Log de erros em ~/.pomodoro.log

Internacionalização (i18n) básica

