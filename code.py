import random
import pygame

pygame.init()

# for display orientation
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# for color of snake and food 
snake_colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]
food_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
black = (0, 0, 0)
blue = (0, 0, 255)

# for snake movements(speed)
snake_block = 10
snake_speed = 10

# for snake direction
snake_list = []
snake_length = 1
snake_direction = "RIGHT"
change_to = snake_direction

# for Snake initial position
snake_head = [width / 2, height / 2]

# Food position
apple_position = [random.randrange(1, (width // snake_block)) * snake_block,
                  random.randrange(1, (height // snake_block)) * snake_block]

# score start with zero
score = 0

# a function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, snake_colors[color_index], [block[0], block[1], snake_block, snake_block])

# a function to display the score
def your_score(score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render("Your Score: " + str(score), True, blue)
    display.blit(score_text, [0, 0])

# the main game loop
game_over = False
color_index = 0
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # changing snake directions
    if change_to == "UP" and not snake_direction == "DOWN":
        snake_direction = "UP"
    elif change_to == "DOWN" and not snake_direction == "UP":
        snake_direction = "DOWN"
    elif change_to == "LEFT" and not snake_direction == "RIGHT":
        snake_direction = "LEFT"
    elif change_to == "RIGHT" and not snake_direction == "LEFT":
        snake_direction = "RIGHT"

    # control to move the snake
    if snake_direction == "UP":
        snake_head[1] -= snake_block
    elif snake_direction == "DOWN":
        snake_head[1] += snake_block
    elif snake_direction == "LEFT":
        snake_head[0] -= snake_block
    elif snake_direction == "RIGHT":
        snake_head[0] += snake_block

    # for collisions with the boundaries
    if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
        game_over = True
        color_index = (color_index + 1) % len(snake_colors)

    # for snake biting itself scenario
    for block in snake_list[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            game_over = True
            color_index = (color_index + 1) % len(snake_colors)

    # to check if the snake has eaten the apple
    if snake_head[0] == apple_position[0] and snake_head[1] == apple_position[1]:
        apple_position = [random.randrange(1, (width // snake_block)) * snake_block,
                          random.randrange(1, (height // snake_block)) * snake_block]
        snake_length += 1
        score += 10  
        
    # to update the display
    display.fill(black)
    draw_snake(snake_block, snake_list)
    pygame.draw.rect(display, food_colors[color_index], [apple_position[0], apple_position[1], snake_block, snake_block])
    your_score(score)  # Update the score rendering

    # to update the snake list
    snake_head_copy = list(snake_head)
    snake_list.append(snake_head_copy)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # to refresh the display
    pygame.display.update()

    # control snake speed
    pygame.time.Clock().tick(snake_speed)

# Quit Pygame
pygame.quit()
