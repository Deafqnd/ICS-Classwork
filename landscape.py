import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

cloud_x1 = 200
cloud_x1_speed = 5

cloud_x2 = 550
cloud_x2_speed = 5

mcl_x = 200
mcl_x_speed = 15

rb_x = 50
rb_x_speed = 16

sf_x = 0
sf_x_speed = 14

sun_x = 300
sun_x_speed = 1

people_x1 = 300
people_x_speed = 15

guardrail_x = 40
guardrail_x_speed = 15

brightness = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sun_x -= sun_x_speed
    if sun_x <= -300:
        sun_x_speed = 0

    cloud_x1 -= cloud_x1_speed
    if cloud_x1 <= -300:
        cloud_x1_speed = 700
    
    cloud_x2 -= cloud_x2_speed
    if cloud_x2 <= -300:
        cloud_x2 = 700

    people_x1 -= people_x_speed
    if people_x1 <= -500:
        people_x1 = 1000

    mcl_x += mcl_x_speed
    if mcl_x > 700:
        mcl_x = -700
    
    rb_x += rb_x_speed
    if rb_x > 700:
        rb_x = -700

    sf_x += sf_x_speed
    if sf_x > 700:
        sf_x = -700

    guardrail_x -= guardrail_x_speed
    if guardrail_x <= -2000:
        guardrail_x = 500

    if brightness < 255:
        brightness += 1
        
    screen.fill('#87ceeb')

    pygame.draw.circle(screen, (255, 255, 0), (sun_x, 110), 50)

    pygame.draw.rect(screen, ('#A9ADB2'), (people_x1 + 332, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 + 351, 320), 20)

    pygame.draw.rect(screen, ('#F545A3'), (people_x1 + 282, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 + 301, 320), 20)

    pygame.draw.rect(screen, ('#F264F7'), (people_x1 + 232, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 + 251, 320), 20)

    pygame.draw.rect(screen, ('#F78964'), (people_x1 + 182, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 + 201, 320), 20)

    pygame.draw.rect(screen, ('#F2B90D'), (people_x1 + 132, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 + 151, 320), 20)

    pygame.draw.rect(screen, ('#0DF2B1'), (people_x1 + 82, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 + 101, 320), 20)

    pygame.draw.rect(screen, ('#088F9B'), (people_x1 + 32, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 + 50, 320), 20)

    pygame.draw.rect(screen, ('#ED3B07'), (people_x1 - 19, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1, 320), 20)

    pygame.draw.rect(screen, ('#2234D4'), (people_x1 - 69, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 - 50, 320), 20)

    pygame.draw.rect(screen, ('#5AE24B'), (people_x1 - 119, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 - 100, 320), 20)

    pygame.draw.rect(screen, ('#DC73E8'), (people_x1 - 169, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 - 150, 320), 20)

    pygame.draw.rect(screen, ('#FFE75C'), (people_x1 - 219, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 - 200, 320), 20)

    pygame.draw.rect(screen, ('#FF2E2E'), (people_x1 - 269, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 - 250, 320), 20)

    pygame.draw.rect(screen, ('#64ABF7'), (people_x1 - 319, 335, 40, 90))
    pygame.draw.circle(screen, ('#FCE6BB'), (people_x1 - 300, 320), 20)

    pygame.draw.rect(screen, ('#C1C4C8'), (0, 370, 1000, 20))
    pygame.draw.rect(screen, ('#C1C4C8'), (0, 340, 1000, 20))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 200, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 400, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 600, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 800, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 1000, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 1200, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 1400, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 1600, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 1800, 340, 20, 60))
    pygame.draw.rect(screen, ('#C1C4C8'), (guardrail_x + 2000, 340, 20, 60))

    pygame.draw.circle(screen, (250, 250, 250), (cloud_x1, 100), 40)
    pygame.draw.circle(screen, (250, 250, 250), (cloud_x1 + 40, 85), 40)
    pygame.draw.circle(screen, (250, 250, 250), (cloud_x1 + 70, 110), 40)
    pygame.draw.circle(screen, (250, 250, 250), (cloud_x1 + 40, 110), 40)

    pygame.draw.circle(screen, (250, 250, 250), (cloud_x2, 85), 50)
    pygame.draw.circle(screen, (250, 250, 250), (cloud_x2 + 50, 70), 50)
    pygame.draw.circle(screen, (250, 250, 250), (cloud_x2 + 80, 105), 50)
    pygame.draw.circle(screen, (250, 250, 250), (cloud_x2 + 50, 105), 50)

    pygame.draw.rect(screen, (255, 0, 0), (sf_x, 360, 250, 50))
    pygame.draw.rect(screen, (255, 0, 0), (sf_x, 320, 25, 50))
    pygame.draw.rect(screen, (255, 0, 0), (sf_x + 250, 380, 40, 20))
    pygame.draw.rect(screen, (255, 0, 0), (sf_x + 40, 342, 120, 25))
    pygame.draw.circle(screen, (0, 0, 0), (sf_x + 25, 380), 20)
    pygame.draw.circle(screen, (0, 0, 0), (sf_x + 225, 380), 20)

    pygame.draw.rect(screen, (255, 100, 0), (mcl_x, 360, 250, 50))
    pygame.draw.rect(screen, (255, 100, 0), (mcl_x, 320, 25, 50))
    pygame.draw.rect(screen, (255, 100, 0), (mcl_x + 250, 380, 40, 20))
    pygame.draw.rect(screen, (255, 100, 0), (mcl_x + 40, 342, 120, 25))
    pygame.draw.circle(screen, (0, 0, 0), (mcl_x + 25, 380), 20)
    pygame.draw.circle(screen, (0, 0, 0), (mcl_x + 225, 380), 20)

    pygame.draw.rect(screen, (0, 0, 125), (rb_x, 360, 250, 50))
    pygame.draw.rect(screen, (0, 0, 125), (rb_x, 320, 25, 50))
    pygame.draw.rect(screen, (0, 0, 125), (rb_x + 250, 380, 40, 20))
    pygame.draw.rect(screen, (0, 0, 125), (rb_x + 40, 342, 120, 25))
    pygame.draw.circle(screen, (0, 0, 0), (rb_x + 25, 380), 20)
    pygame.draw.circle(screen, (0, 0, 0), (rb_x + 225, 380), 20)

    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 1000, 200))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
