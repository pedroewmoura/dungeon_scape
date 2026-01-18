import pgzrun
import sys
from pygame import Rect
from game_logic import Hero, Enemy

WIDTH, HEIGHT = 800, 600
TITLE = "Dungeon Escape: Stealth Master"

GRID_SIZE = 40
OFFSET_X, OFFSET_Y = 100, 80
GAME_STATE = "MENU"
music_enabled = True

hero = None
enemies = []
portal = Rect(OFFSET_X + 14 * GRID_SIZE, OFFSET_Y + 10 * GRID_SIZE, GRID_SIZE, GRID_SIZE)

def setup_game():
    global hero, enemies
    hero = Hero(1, 1, GRID_SIZE, OFFSET_X, OFFSET_Y)
    enemies = [
        Enemy(5, 2, [(5, 2), (10, 2)], GRID_SIZE, OFFSET_X, OFFSET_Y),
        Enemy(2, 8, [(2, 8), (12, 8)], GRID_SIZE, OFFSET_X, OFFSET_Y),
        Enemy(13, 10, [(13, 10), (13, 8), (14, 8)], GRID_SIZE, OFFSET_X, OFFSET_Y)
    ]

def draw():
    screen.fill((10, 5, 5))
    if GAME_STATE == "MENU":
        draw_menu()
    elif GAME_STATE == "PLAYING":
        draw_game()
    elif GAME_STATE == "GAME_OVER":
        screen.draw.text("GAME OVER", center=(400, 300), fontsize=60, color="red")
    elif GAME_STATE == "WIN":
        screen.draw.text("VOCE VENCEU!", center=(400, 300), fontsize=60, color="gold")

def draw_menu():
    screen.draw.text(TITLE, center=(400, 150), fontsize=50, color="red")
    draw_button("Começar Jogo", (400, 300))
    audio_text = "Som: LIGADO" if music_enabled else "Som: DESLIGADO"
    draw_button(audio_text, (400, 380))
    draw_button("Sair", (400, 460))

def draw_button(text, pos):
    button_rect = Rect(0, 0, 250, 50)
    button_rect.center = pos
    screen.draw.filled_rect(button_rect, (60, 0, 0))
    screen.draw.text(text, center=pos, fontsize=30, color="white")

def draw_game():
    arena = Rect(OFFSET_X, OFFSET_Y, 15 * GRID_SIZE, 11 * GRID_SIZE)
    screen.draw.filled_rect(arena, (30, 20, 20))
    screen.draw.filled_rect(portal, (0, 255, 255))
    
    for enemy in enemies:
        screen.blit(enemy.get_sprite(), enemy.pos)
    
    # LOGICA DE INVISIBILIDADE: Só desenha se estiver andando
    if hero.state == "walk":
        screen.blit(hero.get_sprite(), hero.pos)
    else:
        # Se quiser que ele fique levemente visível em vez de sumir total:
        # screen.blit(hero.get_sprite(), hero.pos, alpha=100)
        screen.draw.text("MODO INVISÍVEL", (WIDTH/2 - 50, 20), color="cyan")

    screen.draw.text(f"HP: {hero.health}", (20, 20), fontsize=30, color="red")

def update(dt):
    global GAME_STATE
    if GAME_STATE != "PLAYING": return

    hero.update(dt)
    if hero.grid_pos == (14, 10):
        GAME_STATE = "WIN"
        return

    for enemy in enemies:
        enemy.update(dt)
        # LOGICA DE IMUNIDADE: Só toma dano se estiver em movimento (walk)
        if hero.state == "walk" and hero.collide_with(enemy):
            hero.health -= 1
            # Reseta o herói para a posição inicial para evitar perder tudo de uma vez
            hero.grid_x, hero.grid_y = 1, 1
            hero.target_pos = [1 * GRID_SIZE + OFFSET_X, 1 * GRID_SIZE + OFFSET_Y]
            hero.pos = [hero.target_pos[0], hero.target_pos[1]]

    if hero.health <= 0:
        GAME_STATE = "GAME_OVER"
        music.stop()

def on_mouse_down(pos):
    global GAME_STATE, music_enabled
    if GAME_STATE == "MENU":
        if 275 < pos[1] < 325:
            setup_game()
            GAME_STATE = "PLAYING"
            if music_enabled: music.play("fundo")
        elif 355 < pos[1] < 405:
            music_enabled = not music_enabled
            if not music_enabled: music.stop()
        elif 435 < pos[1] < 485: sys.exit()
    elif GAME_STATE in ["GAME_OVER", "WIN"]:
        GAME_STATE = "MENU"

def on_key_down(key):
    if GAME_STATE == "PLAYING":
        if key in (keys.W, keys.UP): hero.move(0, -1)
        elif key in (keys.S, keys.DOWN): hero.move(0, 1)
        elif key in (keys.A, keys.LEFT): hero.move(-1, 0)
        elif key in (keys.D, keys.RIGHT): hero.move(1, 0)

pgzrun.go()