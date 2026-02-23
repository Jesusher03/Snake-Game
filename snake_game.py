import pygame
import sys
import random

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")

clock = pygame.time.Clock()

dx = 0
dy = 0

snake_head_color = (255,64,0)
snake_body_color = (255,75,8)

snake_x=300
snake_y=300

snake_size = 20
snake = [[snake_x,snake_y]]

food_x = random.randrange(0, width,snake_size)
food_y = random.randrange(0, height,snake_size)

game_over = False
font = pygame.font.SysFont(None, 48)

eat_sound = pygame.mixer.Sound("eat.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            dx = -snake_size
            dy = 0
        if keys[pygame.K_RIGHT]:
            dx = snake_size
            dy = 0
        if keys[pygame.K_UP]:
            dx = 0
            dy = -snake_size
        if keys[pygame.K_DOWN]:
            dx = 0
            dy = snake_size

        new_head = [snake[0][0] + dx, snake[0][1] + dy]
        if(new_head[0]< 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height):
            game_over = True
            gameover_sound.play()

        if new_head in snake[1:]:
            game_over = True
            gameover_sound.play()

        snake.insert(0, new_head)

        #Comer comida
        if new_head[0] == food_x and new_head[1] == food_y:
            eat_sound.play()
            food_x = random.randrange(0, width, snake_size)
            food_y = random.randrange(0, height, snake_size)
        else:
            snake.pop()

        screen.fill((0,0,0))

        pygame.draw.rect(screen, (0,255,0), (food_x, food_y, snake_size, snake_size))

        for index, segment in enumerate(snake):
            if index == 0:
                pygame.draw.rect(screen, snake_head_color,(segment[0], segment[1], snake_size, snake_size))
                pygame.draw.circle(screen, (0,0,0), (segment[0]+5, segment[1]+5), 3)
                pygame.draw.circle(screen, (0,0,0), (segment[0]+15, segment[1]+5), 3)
            else:
                pygame.draw.rect(screen, snake_body_color,(segment[0], segment[1], snake_size, snake_size))
        #SCORE
        score =len(snake) - 1
        score_text = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_text,(10,10))


    else:
        screen.fill((0,0,0))
        text = font.render(f"GAME OVER - Score: {score}", True, (255,255,255))
        screen.blit(text, (120,250))

        restart_text = font.render("PRESS R TO RESTART", True, (255,255,255))
        screen.blit(restart_text, (120,300))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            snake = [[300,300]]
            dx = 0
            dy = 0
            game_over = False


    pygame.display.flip()
    clock.tick(8)




