import pygame

SCREEN_WIDTH=900
SCREEN_HEIGHT=650
Start_X = 50
Start_Y = 50
Line_Span = 60

player1Color = 1
player2Color = 2
overColor = 3

BG_COLOR=pygame.Color(200, 200, 200)
Line_COLOR=pygame.Color(255, 255, 200)
TEXT_COLOR=pygame.Color(255, 0, 0)

# 定义颜色
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

repeat = 0

pieces_images = {
    'b_rook': pygame.image.load("imgs/s2/b_c.gif"),
    'b_elephant': pygame.image.load("imgs/s2/b_x.gif"),
    'b_king': pygame.image.load("imgs/s2/b_j.gif"),
    'b_knigh': pygame.image.load("imgs/s2/b_m.gif"),
    'b_mandarin': pygame.image.load("imgs/s2/b_s.gif"),
    'b_cannon': pygame.image.load("imgs/s2/b_p.gif"),
    'b_pawn': pygame.image.load("imgs/s2/b_z.gif"),

    'r_rook': pygame.image.load("imgs/s2/r_c.gif"),
    'r_elephant': pygame.image.load("imgs/s2/r_x.gif"),
    'r_king': pygame.image.load("imgs/s2/r_j.gif"),
    'r_knigh': pygame.image.load("imgs/s2/r_m.gif"),
    'r_mandarin': pygame.image.load("imgs/s2/r_s.gif"),
    'r_cannon': pygame.image.load("imgs/s2/r_p.gif"),
    'r_pawn': pygame.image.load("imgs/s2/r_z.gif"),
}
