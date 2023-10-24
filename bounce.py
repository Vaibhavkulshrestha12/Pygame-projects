import sys, pygame

pygame.init()

size = width, height = 680,500
dx = 1
dy = 1
x= 150
y = 110
black = (150,150,150)
white = (200,200,200)

screen = pygame.display.set_mode(size)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx

    if y < 0 or y > height:
        dy = -dy

    screen.fill(black)

    pygame.draw.circle(screen, white, (x,y), 8)

    pygame.display.flip()