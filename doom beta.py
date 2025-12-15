import pygame
import math
import sys
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doom Beta 3D Texturizado")


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)


wall_texture = pygame.image.load("wall.png").convert()
enemy_sprite = pygame.image.load("enemy.png").convert_alpha()
bullet_sprite = pygame.Surface((5,5))
bullet_sprite.fill((255,255,0))


MAP = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1]
]

MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)
TILE = 64

player_x = 100
player_y = 100
player_angle = 0
player_speed = 3
rot_speed = 0.05
vida = 10

enemies = [[400,300,3],[500,400,3]]


bullets = []


font = pygame.font.SysFont(None,36)


def raycasting():
    num_rays = 120
    fov = math.pi/3
    start_angle = player_angle - fov/2

    for ray in range(num_rays):
        angle = start_angle + ray*fov/num_rays
        for depth in range(0,1000,2):
            x = player_x + math.cos(angle)*depth
            y = player_y + math.sin(angle)*depth
            map_x = int(x/TILE)
            map_y = int(y/TILE)
            if 0<=map_x<MAP_WIDTH and 0<=map_y<MAP_HEIGHT:
                if MAP[map_y][map_x]==1:
                    
                    proj_height = 600/(depth+0.0001)*70
                    
                    tx = int((x%TILE)/TILE*wall_texture.get_width())
                    wall_column = wall_texture.subsurface(tx,0,1,wall_texture.get_height())
                    wall_column = pygame.transform.scale(wall_column,(7,int(proj_height)))
                    screen.blit(wall_column,(ray*7, HEIGHT/2 - proj_height/2))
                    break


def draw_minimap():
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            rect = pygame.Rect(x*TILE//8, y*TILE//8, TILE//8, TILE//8)
            color = WHITE if MAP[y][x]==1 else BLACK
            pygame.draw.rect(screen,color,rect)
    pygame.draw.circle(screen, BLUE, (int(player_x//8), int(player_y//8)), 5)
    for e in enemies:
        pygame.draw.circle(screen, RED, (int(e[0]//8), int(e[1]//8)), 5)


clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            bullets.append([player_x,player_y,player_angle])

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_x += math.cos(player_angle)*player_speed
        player_y += math.sin(player_angle)*player_speed
    if keys[pygame.K_s]:
        player_x -= math.cos(player_angle)*player_speed
        player_y -= math.sin(player_angle)*player_speed
    if keys[pygame.K_a]:
        player_angle -= rot_speed
    if keys[pygame.K_d]:
        player_angle += rot_speed

    
    if MAP[int(player_y/TILE)][int(player_x/TILE)]==1:
        player_x -= math.cos(player_angle)*player_speed
        player_y -= math.sin(player_angle)*player_speed

    
    for e in enemies:
        if e[0]<player_x: e[0]+=1
        if e[0]>player_x: e[0]-=1
        if e[1]<player_y: e[1]+=1
        if e[1]>player_y: e[1]-=1

    
    for b in bullets[:]:
        b[0] += math.cos(b[2])*10
        b[1] += math.sin(b[2])*10
        screen.blit(bullet_sprite,(b[0],b[1]))
        for e in enemies:
            enemy_rect = pygame.Rect(e[0]-16,e[1]-16,32,32)
            if enemy_rect.collidepoint(b[0],b[1]):
                e[2]-=1
                if e[2]<=0:
                    enemies.remove(e)
                if b in bullets:
                    bullets.remove(b)
        if b[0]<0 or b[0]>WIDTH or b[1]<0 or b[1]>HEIGHT:
            bullets.remove(b)

    
    player_rect = pygame.Rect(player_x-10, player_y-10, 20, 20)
    for e in enemies:
        enemy_rect = pygame.Rect(e[0]-16,e[1]-16,32,32)
        if player_rect.colliderect(enemy_rect):
            vida-=1
            e[0] = random.randint(64,WIDTH-64)
            e[1] = random.randint(64,HEIGHT-64)

    
    raycasting()

    
    for e in enemies:
        screen.blit(enemy_sprite, (e[0]-16, e[1]-16))

    
    draw_minimap()

    
    img = font.render(f'Vida: {vida}',True,WHITE)
    screen.blit(img,(10,10))

    
    if vida<=0:
        img = font.render("Você morreu! Fim de jogo.", True, RED)
        screen.blit(img,(WIDTH//4,HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running=False

    pygame.display.flip()
    clock.tick(60)
