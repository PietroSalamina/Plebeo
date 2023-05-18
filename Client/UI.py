import pygame
from ui_content import button
import player
from pygame.locals import *

pygame.init()

#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
clock = pygame.time.Clock()
fullscreen = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Main Menu")

#game variables
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("Plebeo/Client/ui_content/images/button_resume.png").convert_alpha()
options_img = pygame.image.load("Plebeo/Client/ui_content/images/button_options.png").convert_alpha()
quit_img = pygame.image.load("Plebeo/Client/ui_content/images/button_quit.png").convert_alpha()
video_img = pygame.image.load('Plebeo/Client/ui_content/images/button_video.png').convert_alpha()
audio_img = pygame.image.load('Plebeo/Client/ui_content/images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('Plebeo/Client/ui_content/images/button_keys.png').convert_alpha()
back_img = pygame.image.load('Plebeo/Client/ui_content/images/button_back.png').convert_alpha()

'''
#create button instances
resume_button = button.Button(screen.get_width()/2, 125, resume_img, 1)
fullscreen_button = button.Button(screen.get_width()/2, 125, resume_img, 1)
options_button = button.Button(screen.get_width()/2, 250, options_img, 1)
quit_button = button.Button(screen.get_width()/2, 375, quit_img, 1)
video_button = button.Button(screen.get_width()/2, 75, video_img, 1)
audio_button = button.Button(screen.get_width()/2, 200, audio_img, 1)
keys_button = button.Button(screen.get_width()/2, 325, keys_img, 1)
back_button = button.Button(screen.get_width()/2, 450, back_img, 1)
'''

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


#game loop
run = True
while run:

    #create button instances
    
    fullscreen_button = button.Button(screen.get_width()/2, 125, resume_img, 1)
    options_button = button.Button(screen.get_width()/2, 250, options_img, 1)
    quit_button = button.Button(screen.get_width()/2, 375, quit_img, 1)
    video_button = button.Button(screen.get_width()/2, 75, video_img, 1)
    audio_button = button.Button(screen.get_width()/2, 200, audio_img, 1)
    keys_button = button.Button(screen.get_width()/2, 325, keys_img, 1)
    back_button = button.Button(screen.get_width()/2, 450, back_img, 1)

    screen.fill((52, 78, 91))
    draw_text('Prova', font, 'black', 0,0)

    # check menu state
    if menu_state == "main":
        resume_button = button.Button(screen.get_width()/2, 125, resume_img, 1)
      # draw pause screen buttons
        resume_button.draw(screen)
        if options_button.draw(screen):
            menu_state = "options"
        if quit_button.draw(screen):
            run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
        if video_button.draw(screen):
            menu_state = "video"
        if audio_button.draw(screen):
            print("Audio Settings")
        if back_button.draw(screen):
            menu_state = "main"
    if menu_state == "video":
        if back_button.draw(screen):
            menu_state = "options"
        if fullscreen_button.draw(screen):
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((screen.get_width(),screen.get_height()), pygame.RESIZABLE)

        
            

  #event handler
    for event in pygame.event.get():
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
        if event.type == VIDEORESIZE:
           if not fullscreen:
                screen = pygame.display.set_mode((event.w,event.h), pygame.RESIZABLE)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()