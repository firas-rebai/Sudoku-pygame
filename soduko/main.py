import pygame
import sys
import random
import math

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
dimension = height, width = 1000, 600
screen = pygame.display.set_mode(dimension)
pygame.display.set_caption("Sudoku by Firas")
sudoku_table = pygame.image.load("soduko_grid.png")
check_button = pygame.image.load("check.png")
selected_img = pygame.image.load("selected.png")
wrong_img = pygame.image.load("wrong.png")
start_button = pygame.image.load("start_button.png")
pause_button = pygame.image.load("pause_button.png")
restart_button = pygame.image.load("restart_button.png")
font = pygame.font.Font('Navada Demo.otf', 60)
table = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

numbers = []

for i in range(10):
    if i != 0:
        numbers.append(pygame.image.load(str(i) + ".png"))


def check(t, x, y, num):
    for i in range(9):
        if t[x][i] == num:
            return False
    for i in range(9):
        if t[i][y] == num:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if t[x0 + i][y0 + j] == num:
                return False
    return True


static_table = [[0 for i in range(9)] for i in range(9)]
n = 20
while n != 0:
    x = random.randint(0, 8)
    y = random.randint(0, 8)
    num = random.randint(1, 9)
    if table[x][y] == 0 and check(table, x, y, num):
        table[x][y] = num
        static_table[x][y] = num
        n -= 1

wrong_table = [[0 for i in range(9)] for i in range(9)]

for i in range(9):
    print(table[i])


def print_nums(table):
    for i in range(9):
        for j in range(9):
            if table[i][j] != 0:
                screen.blit(numbers[table[i][j] - 1], (24 + (j * 60), 30 + (i * 60)))


def print_wrong(t):
    for i in range(9):
        for j in range(9):
            if t[i][j] == 1:
                screen.blit(wrong_img, (24 + (j * 60), 24 + (i * 60)))


def check_all(t, wrong_state):
    for i in range(9):
        for j in range(9):
            if t[i][j] == 0 or wrong_state:
                return False


def change_num(sx, sy, num):
    global table
    global wrong_table
    global static_table
    if table[sx][sy] != num and static_table[sx][sy] == 0:
        if not check(table, sx, sy, num):
            wrong_table[sx][sy] = 1
        elif check(table, sx, sy, num):
            wrong_table[sx][sy] = 0
        if static_table[sx][sy] == 0:
            table[sx][sy] = num


def mouse_click(x, y, w, h):
    mouse_cor = pygame.mouse.get_pos()
    if y < mouse_cor[1] < y + h and x < mouse_cor[0] < x + w and pygame.mouse.get_pressed() == (1, 0, 0):
        return True
    else:
        return False


win = False
wrong = False
running = True
selected_pos = [24, 24]
pause_text = font.render("Paused", True, (0, 0, 0), (64, 64, 64))
win_text = font.render("You Won", True, (255, 0, 0), (64, 64, 64))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP and running:
            sx = (selected_pos[1] - 24) // 60
            sy = (selected_pos[0] - 24) // 60
            if event.key == pygame.K_UP:
                if not (selected_pos[1] - 61) < 24:
                    selected_pos[1] -= 61
            if event.key == pygame.K_DOWN:
                if not selected_pos[1] + 61 > 564:
                    selected_pos[1] += 61
            if event.key == pygame.K_RIGHT:
                if not selected_pos[0] + 60 > 564:
                    selected_pos[0] += 61
            if event.key == pygame.K_LEFT:
                if not selected_pos[0] - 60 < 24:
                    selected_pos[0] -= 61
            if event.key == pygame.K_KP0:
                if static_table[sx][sy] == 0:
                    table[sx][sy] = 0
                    wrong_table[sx][sy] = 0
            if event.key == pygame.K_KP1:
                change_num(sx, sy, 1)
            if event.key == pygame.K_KP2:
                change_num(sx, sy, 2)
            if event.key == pygame.K_KP3:
                change_num(sx, sy, 3)
            if event.key == pygame.K_KP4:
                change_num(sx, sy, 4)
            if event.key == pygame.K_KP5:
                change_num(sx, sy, 5)
            if event.key == pygame.K_KP6:
                change_num(sx, sy, 6)
            if event.key == pygame.K_KP7:
                change_num(sx, sy, 7)
            if event.key == pygame.K_KP8:
                change_num(sx, sy, 8)
            if event.key == pygame.K_KP9:
                change_num(sx, sy, 9)

    # check ,pause and restart button -----------------
    if mouse_click(690, 490, 180, 70) and check_all(wrong_table, wrong):
        print("correct")
        win = True
    elif mouse_click(690, 490, 180, 70) and check_all(wrong_table, wrong) is False:
        print("hewwo UwU")
    if mouse_click(895, 95, 75, 75) and running:
        running = False
    elif mouse_click(895, 95, 75, 75) and running is False:
        running = True
    """if mouse_click(895, 195, 75, 75) and running:
        print("2")
        while n != 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            num = random.randint(1, 9)
            if table[x][y] == 0 and check(table, x, y, num):
                table[x][y] = num
                static_table[x][y] = num
                n -= 1"""
    # -------------buttons and backgrounds ----
    screen.fill((50, 50, 50))
    screen.blit(sudoku_table, (0, 0))
    pygame.draw.rect(screen, green, [690, 490, 180, 70])
    pygame.draw.rect(screen, blue, [895, 195, 75, 75])
    pygame.draw.rect(screen, blue, [895, 95, 75, 75])
    screen.blit(check_button, (700, 500))
    if running is False:
        screen.blit(start_button, (900, 100))
    else:
        screen.blit(pause_button, (900, 100))
    screen.blit(restart_button, (900, 200))
    # print(pygame.mouse.get_pos())
    # ---------------printing the table----------------
    print_nums(table)
    # --------selected pause and wrong answer /// winning message--------
    screen.blit(selected_img, selected_pos)
    print_wrong(wrong_table)
    if running is False:
        pygame.draw.rect(screen, (64, 64, 64), [350, 250, 300, 100])
        screen.blit(pause_text, (400, 250))
    if win:
        pygame.draw.rect(screen, (64, 64, 64), [350, 250, 300, 100])
        screen.blit(win_text, (400, 500))
    pygame.display.update()
