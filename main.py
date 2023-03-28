import pygame
from random import randrange

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500,540))
pygame.display.set_caption("funny snake")
clock = pygame.time.Clock()
run = True

record = str(open('record.txt').read())

f1 = pygame.font.Font(None, 36)
text = f1.render('счёт: 0', True, (0, 0, 0))
rec = f1.render("рекорд: " + record, True, (0, 0, 0))

head = [pygame.image.load('sprites/right.png'), pygame.image.load('sprites/left.png'), pygame.image.load('sprites/up.png'),pygame.image.load('sprites/down.png')]
tail = [pygame.image.load('sprites/tail_right.png'), pygame.image.load('sprites/tail_left.png'), pygame.image.load(
    'sprites/tail_up.png'), pygame.image.load(
    'sprites/tail_down.png')]
orange = pygame.image.load('sprites/orange.png')
body = [pygame.image.load('sprites/body.png'), pygame.image.load('sprites/body_2.png')]

x = 203
y = 235

start = False
score = 0

movedirection = "right"

keys = pygame.key.get_pressed()

predx = 203
predy = 235

length = [(203, 235, movedirection), (203, 235, movedirection)]
food = []

def snake():
    if movedirection == "right":
        screen.blit(head[0], length[-1][:-1])
    elif movedirection == "left":
        screen.blit(head[1], length[-1][:-1])
    elif movedirection == "up":
        screen.blit(head[2], length[-1][:-1])
    elif movedirection == "down":
        screen.blit(head[3], length[-1][:-1])
    if length[0][2] == "right":
        screen.blit(tail[0], length[0][:-1])
    elif length[0][2] == "left":
        screen.blit(tail[1], length[0][:-1])
    elif length[0][2] == "up":
        screen.blit(tail[2], length[0][:-1])
    elif length[0][2] == "down":
        screen.blit(tail[3], length[0][:-1])
    for x in range(1, len(length) - 1):
        if length[x][2] == "right" or length[x][2] == "left":
            screen.blit(body[0], length[x][:-1])
        elif length[x][2] == "up" or length[x][2] == "down":
            screen.blit(body[1], length[x][:-1])


def game():
    global movedirection, x, y, start, predx, predy, length, food, score, text, record, rec
    screen.fill((235, 19, 19))
    pygame.draw.rect(screen, (0, 0, 0), (7, 7, 488, 488))
    '''for d in range(42, 481, 32):
        pygame.draw.line(screen, (255, 255, 255), (d, 10), (d, 489), 1)
        pygame.draw.line(screen, (255, 255, 255), (10, d), (489, d), 1)'''
    if x >= 490 or x < 10 or y >= 490 or y < 10:
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 500, 500))
        pygame.display.update()
        x = 203
        y = 235
        length = [(203, 235, "right"), (203, 235, "right")]
        movedirection = "right"
        start = False
        score = 0
        text = f1.render('счёт: 0', True, (0, 0, 0))
        record = str(open('record.txt').read())
        rec = f1.render("рекорд: " + record, True, (0, 0, 0))
        return
    if movedirection == "right":
        x += 16
    elif movedirection == "down":
        y += 16
    elif movedirection == "up":
        y -= 16
    elif movedirection == "left":
        x -= 16
    if keys[pygame.K_RIGHT] and movedirection != "left":
        movedirection = "right"
    if keys[pygame.K_DOWN] and movedirection != "up":
        movedirection = "down"
    if keys[pygame.K_LEFT] and movedirection != "right":
        movedirection = "left"
    if keys[pygame.K_UP] and movedirection != "down":
        movedirection = "up"
    if len(food) < 1:
        edx = randrange(11, 458, 16)
        edy = randrange(11, 458, 16)
        if length.count((edx, edy, "left")) > 0 or length.count((edx, edy, "right")) > 0 or length.count((edx, edy, "up")) > 0 or length.count((edx, edy, "down")) > 0:
            pass
        else:
            food.append((edx, edy))

    screen.blit(orange, (food[0]))
    if length.count((x, y, "left")) > 0 or length.count((x, y, "right")) > 0 or length.count((x, y, "up")) > 0 or length.count((x, y, "down")) > 0:
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 500, 500))
        pygame.display.update()
        x = 203
        y = 235
        length = [(203, 235, "right"), (203, 235, "right")]
        movedirection = "right"
        start = False
        score = 0
        text = f1.render('счёт: 0', True, (0, 0, 0))
        record = str(open('record.txt').read())
        rec = f1.render("рекорд: " + record, True, (0, 0, 0))
        return

    if (x == food[0][0]) and (y == food[0][1]):
        length.append((x, y, movedirection))
        food = []
        score += 1
        text = f1.render(f'счёт: {score}', True, (0, 0, 0))
        if score > int(record):
            record = str(score)
            with open("record.txt", "w") as file:
                file.write(str(record))
    else:
        length.append((x, y, movedirection))
        length = length[1:]
    snake()
    screen.blit(text, (25, 505))
    screen.blit(rec, (300, 505))
    pygame.display.update()


while run:
    clock.tick(14)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((235, 19, 19))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start = True
    if start == True:
        game()