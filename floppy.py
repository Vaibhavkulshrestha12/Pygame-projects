import pygame
import random

pygame.init()


WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


bird_x = 100
bird_y = HEIGHT // 2
bird_speed = 1
gravity = 0.3


pipe_width = 50
pipe_gap = 400
pipe_x = WIDTH
pipe_heights = [random.randint(100, 400) for _ in range(3)]
pipe_speed = 5

score = 0
font = pygame.font.Font(None, 36)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = -10

   
    bird_speed += gravity
    bird_y += bird_speed

    
    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_heights = [random.randint(100, 400) for _ in range(3)]
        score += 1

   
    bird_rect = pygame.Rect(bird_x, bird_y, 30, 30)
    for height in pipe_heights:
        pipe_upper = pygame.Rect(pipe_x, 0, pipe_width, height)
        pipe_lower = pygame.Rect(pipe_x, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap)
        if bird_rect.colliderect(pipe_upper) or bird_rect.colliderect(pipe_lower) or bird_y >= HEIGHT:
            running = False

   
    screen.fill(WHITE)

 
    for height in pipe_heights:
        pygame.draw.rect(screen, BLUE, (pipe_x, 0, pipe_width, height))
        pygame.draw.rect(screen, BLUE, (pipe_x, height + pipe_gap, pipe_width, HEIGHT - height - pipe_gap))

   
    pygame.draw.circle(screen, BLUE, (bird_x, int(bird_y)), 15)

    
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

  
    pygame.display.update()

    
    pygame.time.Clock().tick(30)


pygame.quit()
