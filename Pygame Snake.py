import pygame
import time
import random
import pickle
try:
    Highscore = open("High.score","rb")
    high_score = int(pickle.load(Highscore))
    Highscore.close()
except:
    Highscorew = open("High.score","wb")
    pickle.dump("0",Highscorew)
    Highscorew.close()
    high_score = 0

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Pygame Snake')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake
# body
snake_body = [[100, 50]]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# setting default snake direction
# towards right
direction = 'STOP'
change_to = direction
# initial score
score = 0


# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)
def show_high_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('                               High Score : ' + str(high_score), True, color)

    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)
# Main Function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
        if score >= int(high_score):
            high_score = score
            HighScore = open("High.Score", "wb")
            pickle.dump(high_score, HighScore)
            HighScore.close()


    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, "#460F60", pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        time.sleep(1)
        snake_position = [100, 50]
        direction = 'STOP'
        change_to = direction
        score = 0
        snake_body = [[100,50]]
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        time.sleep(1)
        snake_position = [100, 50]
        direction = 'STOP'
        change_to = direction
        score = 0
        snake_body = [[100, 50]]
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            time.sleep(1)
            snake_position = [100, 50]
            direction = 'RIGHT'
            change_to = direction
            score = 0
            snake_body = [[100, 50]]
    # displaying score and high score countinuously
    show_score(1, white, 'Arial', 20)
    show_high_score(1, white, 'Arial', 20)
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)