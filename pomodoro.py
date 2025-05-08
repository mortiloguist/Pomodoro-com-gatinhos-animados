import time
import curses
import platform
import json
import argparse
from datetime import datetime
import os

class PomodoroTimer:
    def __init__(self):
        self.work_time = 25 * 60  # 25 minutos em segundos
        self.short_break = 5 * 60  # 5 minutos em segundos
        self.long_break = 20 * 60  # 20 minutos em segundos
        self.sessions = 4  # Número de sessões antes da pausa longa
        self.current_session = 0
        self.is_running = False
        self.time_left = self.work_time
        self.mode = "work"  # work, short_break, long_break
        self.history = []
        self.start_time = None
        self.animation_frame = 0
        self.animation_speed = 0.5  # segundos por frame
        
        # Frames da animação do gatinho Luna
        self.luna_frames = [
            [
                "  /\\_/\\  ",
                " ( o.o ) ",
                "  > ^ <  ",
                "  /   \\  "
            ],
            [
                "  /\\_/\\  ",
                " ( -.- ) ",
                "  > ^ <  ",
                "  /   \\  "
            ],
            [
                "  /\\_/\\  ",
                " ( ^.^ ) ",
                "  > ^ <  ",
                "  /   \\  "
            ],
            [
                "  /\\_/\\  ",
                " ( -.- ) ",
                "  > ^ <  ",
                "  /   \\  "
            ]
        ]
        
        # Frames da animação do gatinho Artemis
        self.artemis_frames = [
            [
                "  /\\_/\\  ",
                " ( >.< ) ",
                "  > ^ <  ",
                "  /   \\  "
            ],
            [
                "  /\\_/\\  ",
                " ( -.- ) ",
                "  > ^ <  ",
                "  /   \\  "
            ],
            [
                "  /\\_/\\  ",
                " ( ^.^ ) ",
                "  > ^ <  ",
                "  /   \\  "
            ],
            [
                "  /\\_/\\  ",
                " ( -.- ) ",
                "  > ^ <  ",
                "  /   \\  "
            ]
        ]
        
    def start(self):
        curses.wrapper(self.main)
        
    def main(self, stdscr):
        # Configuração inicial do curses
        curses.curs_set(0)  # Esconde o cursor
        stdscr.nodelay(1)  # Não bloqueia na leitura do teclado
        stdscr.timeout(100)  # Timeout de 100ms para atualização da tela
        
        last_animation_time = time.time()
        
        while True:
            try:
                # Limpa a tela
                stdscr.clear()
                
                # Atualiza a animação
                current_time = time.time()
                if current_time - last_animation_time >= self.animation_speed:
                    self.animation_frame = (self.animation_frame + 1) % len(self.luna_frames)
                    last_animation_time = current_time
                
                # Desenha a interface
                self.draw_interface(stdscr)
                
                # Atualiza a tela
                stdscr.refresh()
                
                # Processa input
                key = stdscr.getch()
                if key == ord('q'):
                    break
                elif key == ord(' '):
                    self.toggle_timer()
                elif key == ord('n'):
                    self.next_phase()
                elif key == ord('s'):
                    self.stop_session()
                
                # Atualiza o timer
                if self.is_running:
                    self.update_timer()
                
                # Pequena pausa para não sobrecarregar a CPU
                time.sleep(0.1)
            except curses.error:
                # Se a tela for muito pequena, mostra mensagem de erro
                stdscr.clear()
                stdscr.addstr(0, 0, "Tela muito pequena! Aumente o tamanho da janela.")
                stdscr.refresh()
                time.sleep(1)
    
    def toggle_timer(self):
        if not self.is_running:
            self.start_time = time.time()
        else:
            self.start_time = None
        self.is_running = not self.is_running
    
    def draw_interface(self, stdscr):
        # Obtém dimensões da tela
        height, width = stdscr.getmaxyx()
        
        # Verifica se a tela é grande o suficiente
        min_width = 80
        min_height = 20
        
        if width < min_width or height < min_height:
            raise curses.error("Tela muito pequena")
        
        # Desenha o relógio circular ASCII
        clock = [
            "╭────────────╮",
            f"│  ◯ {self.format_time(self.time_left)}  │",
            "│  \\|||||/  │",
            "╰────────────╯"
        ]
        
        # Centraliza o relógio
        clock_x = (width - len(clock[0])) // 2
        clock_y = (height - len(clock)) // 2
        
        # Desenha o relógio
        for i, line in enumerate(clock):
            if clock_y + i < height:
                stdscr.addstr(clock_y + i, clock_x, line)
        
        # Caixa com nome Luna
        luna_box = [
            "╭──────────╮",
            "│   Luna   │",
            "╰──────────╯"
        ]
        luna_x = max(2, clock_x - len(luna_box[0]) - 5)
        luna_y = max(2, clock_y - len(luna_box) - 1)
        
        # Desenha a caixa Luna
        for i, line in enumerate(luna_box):
            if luna_y + i < height:
                stdscr.addstr(luna_y + i, luna_x, line)
        
        # Desenha o gatinho Luna
        luna = self.luna_frames[self.animation_frame]
        luna_x = max(2, clock_x - len(luna[0]) - 5)
        luna_y = clock_y
        
        # Desenha Luna
        for i, line in enumerate(luna):
            if luna_y + i < height:
                stdscr.addstr(luna_y + i, luna_x, line)
        
        # Caixa com nome Artemis
        artemis_box = [
            "╭────────────╮",
            "│  Artemis   │",
            "╰────────────╯"
        ]
        artemis_x = min(width - len(artemis_box[0]) - 2, clock_x + len(clock[0]) + 5)
        artemis_y = max(2, clock_y - len(artemis_box) - 1)
        
        # Desenha a caixa Artemis
        for i, line in enumerate(artemis_box):
            if artemis_y + i < height:
                stdscr.addstr(artemis_y + i, artemis_x, line)
        
        # Desenha o gatinho Artemis
        artemis = self.artemis_frames[self.animation_frame]
        artemis_x = min(width - len(artemis[0]) - 2, clock_x + len(clock[0]) + 5)
        artemis_y = clock_y
        
        # Desenha Artemis
        for i, line in enumerate(artemis):
            if artemis_y + i < height:
                stdscr.addstr(artemis_y + i, artemis_x, line)
        
        # Desenha informações adicionais
        info_y = min(height - 4, clock_y + len(clock) + 2)
        if info_y < height:
            stdscr.addstr(info_y, clock_x, f"Modo: {self.mode}")
        if info_y + 1 < height:
            stdscr.addstr(info_y + 1, clock_x, f"Sessão: {self.current_session + 1}/{self.sessions}")
        
        # Desenha controles
        controls = "Controles: [Space] Iniciar/Pausar | [n] Próximo | [s] Parar | [q] Sair"
        if height > 0:
            stdscr.addstr(height - 1, max(0, (width - len(controls)) // 2), controls)
    
    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def update_timer(self):
        if self.start_time is None:
            return
            
        elapsed = int(time.time() - self.start_time)
        self.time_left = max(0, self.work_time - elapsed)
        
        if self.time_left <= 0:
            self.next_phase()
            self.start_time = time.time()
    
    def next_phase(self):
        if self.mode == "work":
            self.current_session += 1
            if self.current_session >= self.sessions:
                self.mode = "long_break"
                self.time_left = self.long_break
            else:
                self.mode = "short_break"
                self.time_left = self.short_break
        else:
            self.mode = "work"
            self.time_left = self.work_time
        self.start_time = time.time()
    
    def stop_session(self):
        self.is_running = False
        self.start_time = None
        self.current_session = 0
        self.mode = "work"
        self.time_left = self.work_time

if __name__ == "__main__":
    timer = PomodoroTimer()
    timer.start() 