import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()
pygame.font.init()

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ------------------------------------------------------
# Initialize global variables

score = 0

racer_speed = 10

racer = pygame.Rect(200, 100, 65, 20)


# gracias victor cai
gas_cans = []
for n in range(15):
    g = pygame.Rect(random.randrange(WIDTH), random.randrange(HEIGHT), 15, 30)
    gas_cans.append(g)

cars = []
for n in range(10):
    c = pygame.Rect(random.randrange(WIDTH), random.randrange(HEIGHT), 65, 20)
    cars.append(c)

font_arial_25 = pygame.font.SysFont('Arial', 25)

current_screen = 'menu'

# -----------------------------------------------

running = True

while running: 
    if current_screen == 'menu':
        # Event Handling 1 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    current_screen = 'ayden_instruction_screen'
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        # Game State Updates 1 
        # Math and stuff

        # Drawing 1 
        screen.fill('#090820')

        menu_1 = font_arial_25.render('Welcome!', True, (255, 255, 255))
        menu_2 = font_arial_25.render('Press the i key to continue!', True, (255, 255, 255))
        menu_3 = font_arial_25.render('Press the Escape key at any time to quit', True, (255, 255, 255))

        menu_1_width = menu_1.get_width()
        menu_2_width = menu_2.get_width()
        menu_3_width = menu_3.get_width()

        screen.blit(menu_1, (WIDTH//2 - menu_1_width//2, HEIGHT//2))
        screen.blit(menu_2, (WIDTH//2 - menu_2_width//2, HEIGHT//2 + 30))
        screen.blit(menu_3, (WIDTH//2 - menu_3_width//2, HEIGHT//2 + 60))

    elif current_screen == 'ayden_instruction_screen':
        # Event handling 2 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_screen = 'racer game'
                elif event.key == pygame.K_ESCAPE:
                    current_screen = 'menu'

        # Game State Updates 2 
        # Math and stuff happens here


        # Drawing 2 
        screen.fill('#A0E8E5')

        inst_text_1 = font_arial_25.render('Use WASD to move', True, (0, 0, 0))
        inst_text_2 = font_arial_25.render('Once the timer runs out, it\'s game over!', True, (0, 0, 0))
        inst_text_3 = font_arial_25.render('When you\'re ready, press "1" to start!', True, (0, 0, 0))
        inst_text_4 = font_arial_25.render('Collect all the gas cans to win!', True, (0, 0, 0))

        inst_text_width_1 = inst_text_1.get_width()
        inst_text_width_2 = inst_text_2.get_width()
        inst_text_width_3 = inst_text_3.get_width()
        inst_text_width_4 = inst_text_4.get_width()

        screen.blit(inst_text_1, (WIDTH//2 - inst_text_width_1//2, HEIGHT//2))
        screen.blit(inst_text_2, (WIDTH//2 - inst_text_width_2//2, HEIGHT//2 - 20))
        screen.blit(inst_text_3, (WIDTH//2 - inst_text_width_3//2, HEIGHT//2 - 40))
        screen.blit(inst_text_4, (WIDTH//2 - inst_text_width_4//2, HEIGHT//2 - 60))


    elif current_screen == 'racer game':
        # Event Handling 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = 'ayden_instruction_screen'

        # Game State Updates 3

        # Player 

        keys = pygame.key.get_pressed()

        if keys[119] == True: 
            racer[1] -= racer_speed
            # W key
    
        if keys[97] == True:
            racer[0] -= racer_speed
            # A key
    
        if keys[115] == True:
            racer[1] += racer_speed
            # S key

        if keys[100] == True:
            racer[0] += racer_speed
            # D key

        if racer[0] > 1300:
                racer[0] = -50

        if racer[0] < -50:
            racer[0] = 1300
        
        if racer[1] > 750:
            racer[1] = 50

        if racer[1] < -30:
            racer[1] = 750


        # Gas Cans
        for can in gas_cans:
            can[0] -= 5
            if can[0] <= -50:
                can[0] = 1300
            if racer.colliderect(can):
                score += 1
                gas_cans.remove(can)

        
        # Obstacle Cars
        for car in cars:
            car[0] -= 7
            if car[0] <= -50:
                car[0] = 1300
            if racer.colliderect(car):
                current_screen = "game over!"

        # Win Condition
        if score == 15:
            current_screen = "Win!!!"

        # More math and stuff

        # Drawing 3 
        screen.fill('#CCCCCC')

        # Gas Cans

        for can in gas_cans:
            pygame.draw.rect(screen, ('#F25555'), can)
        
        for car in cars:
            # NPC Car Body
            pygame.draw.rect(screen, (0, 0, 255), car)
            # NPC Rear Left
            pygame.draw.rect(screen, (0, 0, 0), (car[0] + 5, car[1] - 2, 10, 5))
             # NPC Front Left
            pygame.draw.rect(screen, (0, 0, 0), (car[0] + 50, car[1] - 2, 10, 5))
            # NPC Front Right
            pygame.draw.rect(screen, (0, 0, 0), (car[0] + 50, car[1] + 18, 10, 5))
            # NPC Rear Right
            pygame.draw.rect(screen, (0, 0, 0), (car[0] + 5, car[1] + 18, 10, 5))

        # Player Car Body

        pygame.draw.rect(screen, ("#0A7968"), (racer[0], racer[1], 65, 20))
        # Player Rear Left
        pygame.draw.rect(screen, (0, 0, 0), (racer[0] + 5, racer[1] - 2, 10, 5))
        # Player Front Left
        pygame.draw.rect(screen, (0, 0, 0), (racer[0] + 50, racer[1] - 2, 10, 5))
        # Player Front Right
        pygame.draw.rect(screen, (0, 0, 0), (racer[0] + 50, racer[1] + 18, 10, 5))
        # Player Rear Right
        pygame.draw.rect(screen, (0, 0, 0), (racer[0] + 5, racer[1] + 18, 10, 5))

    elif current_screen == 'game over!':
        # Event Handling 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = 'menu'
        
        # Game State Updates 4


        # Drawing 4
        screen.fill('#A0E8E5')

        game_over_1 = font_arial_25.render('You Crashed!', True, (0, 0, 0))
        game_over_2 = font_arial_25.render('Press the Escape Key to return to the menu!', True, (0, 0, 0))
        game_over_3 = font_arial_25.render(f'Your score: {score}! Game over!', True, (0, 0, 0))

        game_over_1_width = game_over_1.get_width()
        game_over_2_width = game_over_2.get_width()
        game_over_3_width = game_over_3.get_width()

        screen.blit(game_over_1, (WIDTH//2 - game_over_1_width//2, HEIGHT//2))
        screen.blit(game_over_2, (WIDTH//2 - game_over_2_width//2, HEIGHT//2 + 30))
        screen.blit(game_over_3, (WIDTH//2 - game_over_3_width//2, HEIGHT//2 + 60))
    
    elif current_screen == 'Win!!!':
        # Event Handling 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = 'menu'

        # Game State Updates 5

        # Drawing 5
        screen.fill('#0A7968')

        win_1 = font_arial_25.render('You Win!', True, (0, 0, 0))
        win_2 = font_arial_25.render(f'Your score: {score}! Congradulations!', True, (0, 0, 0))

        win_1_width = win_1.get_width()
        win_2_width = win_2.get_width()

        screen.blit(win_1, (WIDTH//2 - win_1_width//2, HEIGHT//2))
        screen.blit(win_2, (WIDTH//2 - win_2_width//2, HEIGHT//2 + 30))
    
    # DONT TOUCH THIS OR EVERYTHING BREAKS
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    pygame.display.flip()
    clock.tick(30)
    # ------------------------------------

pygame.quit()
