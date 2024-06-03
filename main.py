import pygame

pygame.init()

screen_H = 600;
screen_W = 600;
Line_WIDTH = 15
Circle_R = 60
Circle_Width = 15
Space = 55
## The Main Screen
Screen = pygame.display.set_mode((screen_W, screen_H))

def draw_lines():
    pygame.draw.line(Screen, (255, 0, 0), (0,200),(600,200),Line_WIDTH)
    pygame.draw.line(Screen, (0, 225, 0), (0,400),(600,400),Line_WIDTH)
    pygame.draw.line(Screen, (0, 0, 255), (200,0),(200,600),Line_WIDTH)
    pygame.draw.line(Screen, (255, 255, 0), (400,0),(400,600),Line_WIDTH)

bored = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]

def isavalable(row,col):
    if bored[row][col] > -1:
        return False
    else:
        return True
def markbored(row,col,player):
    bored[row][col] = player

def draw_board():
    for row in range(0,3):
        for col in range(0,3):
            if bored[row][col] == 2:
                pygame.draw.circle(Screen, (225,0,0),(int(col*200 + 200/2),int(row*200 + 200/2)),Circle_R,Circle_Width)
            elif bored[row][col] == 1:
                pygame.draw.line(Screen, (225, 0, 0), (col * 200 + Space, row * 200 + 200 - Space), (col * 200 + 200 - Space, row * 200 + Space), 15)
                pygame.draw.line(Screen, (225, 0, 0), (col * 200 + Space, row * 200 + Space),(col * 200 + 200 - Space, row * 200 + 200 - Space), 15)

def CheckWin(bored):
    win = False
    for i in range(0, 3):
        if bored[i][0] == bored[i][1] == bored[i][2]:
            win = True
    for i in range(0, 3):
        if bored[0][i] == bored[1][i] == bored[2][i]:
            win = True
    if bored[0][0] == bored[1][1] == bored[2][2] or bored[0][2] == bored[1][1] == bored[2][0]:
        win = True
    return win

run = True

player = 1
counter = 0
draw_lines()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = (int)(event.pos[0]/200)
            y = (int)(event.pos[1]/200)
            if isavalable(y,x):
                counter += 1
                if player == 1:
                    markbored(y,x,player)
                    player = 2
                else:
                    markbored(y,x,player)
                    player = 1
            draw_board()
            if CheckWin(bored) == 1:
                print("The winner is PLayer" + str(bored[x][y]))
                run = False
            if counter == 9:
                print("Draw")
                break
    pygame.display.update()

pygame.quit()
