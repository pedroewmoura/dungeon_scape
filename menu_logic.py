from pygame.rect import Rect
import pygame 

class Button:
    def __init__(self, rect, label, action):
        self.rect = rect
        self.label = label
        self.action = action 
        self.color = (80, 0, 0)

    def draw(self, screen):
        screen.draw.filled_rect(self.rect, self.color)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
             screen.draw.rect(self.rect, (255, 100, 0)) 
        screen.draw.text(self.label, center=self.rect.center, 
                         color=(255, 200, 200), fontsize=30)

def create_menu_buttons(WIDTH, HEIGHT, start_game_func, toggle_audio_func, exit_game_func):
    center_x = WIDTH / 2
    y_start = HEIGHT / 2
    largura, altura = 250, 60
    buttons = []
    buttons.append(Button(Rect(center_x - largura/2, y_start, largura, altura), 
                          "Começar o Jogo", start_game_func))
    buttons.append(Button(Rect(center_x - largura/2, y_start + 80, largura, altura), 
                          "Música/Sons ON/OFF", toggle_audio_func))
    buttons.append(Button(Rect(center_x - largura/2, y_start + 160, largura, altura), 
                          "Saída", exit_game_func))
    return buttons