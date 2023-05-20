import pygame
from random import randrange
pygame.init()
pygame.display.set_caption("Thanks (Tank game)")
gameimage = pygame.image.load('image/Tank1.png')
pygame.display.set_icon(gameimage)
clock = pygame.time.Clock()
W = 1200  # 1600, 800
H = 800
sc = pygame.display.set_mode((W, H))
FPS = 60
hp1 = 200
hp2 = 200
bg = pygame.image.load('image/Background.png').convert_alpha()
bg = pygame.transform.scale(bg, (W, H))
f = pygame.font.SysFont('robotic', 130)
sc_text = f.render(str("Game Over"), 1, (0,0,0))
hero1_image = pygame.image.load('image/Tank1.png').convert_alpha()
hero1_image = pygame.transform.scale(hero1_image, (72, 104))
hero1_rect = hero1_image.get_rect(centerx = W//6, centery = H//2)

hero2_image = pygame.image.load('image/Tank2.png').convert_alpha()
hero2_image = pygame.transform.scale(hero2_image, (72, 104))
hero2_rect = hero1_image.get_rect(centerx = 5*W//6, centery = H//2)

bullet_image = pygame.image.load('image/Bullet.png').convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (12, 20))
bullet_rect = bullet_image.get_rect(centerx = W//2, centery = H//2)

bullet_image2 = pygame.image.load('image/Bullet.png').convert_alpha()
bullet_image2 = pygame.transform.scale(bullet_image2, (12, 20))
bullet_rect2 = bullet_image2.get_rect(centerx = W//2, centery = H//2)

healbox = pygame.image.load('image/BAR FOR HP.png').convert_alpha()
healbox = pygame.transform.scale(healbox, (200, 30))
healbox_rect = healbox.get_rect(centerx = 120, centery = 30)

HP_bar = pygame.image.load('image/HP BAR.png').convert_alpha()
HP_bar = pygame.transform.scale(HP_bar, (200, 30))
HP_bar_rect = HP_bar.get_rect(centerx = 120, centery = 30)

healbox2 = pygame.image.load('image/BAR FOR HP.png').convert_alpha()
healbox2 = pygame.transform.scale(healbox, (200, 30))
healbox_rect2 = healbox.get_rect(centerx = W - 120, centery = 30)

HP_bar2 = pygame.image.load('image/HP BAR.png').convert_alpha()
HP_bar2 = pygame.transform.scale(HP_bar, (200, 30))
HP_bar_rect2 = HP_bar.get_rect(centerx = W - 120, centery = 30)

bonus_image = pygame.image.load('image/heal.png').convert_alpha()
bonus_image = pygame.transform.scale(bonus_image, (70, 70))
bonus_image_rect = bonus_image.get_rect(centerx = W//2, centery = H//2)

bonus_image2 = pygame.image.load('image/Oil.png').convert_alpha()
bonus_image2 = pygame.transform.scale(bonus_image2, (63, 75))
bonus_image_rect2 = bonus_image2.get_rect(centerx = W//2, centery = H//2)

mine_image = pygame.image.load('image/Mine.png').convert_alpha()
mine_image = pygame.transform.scale(mine_image, (65, 65))
mine_image_rect = mine_image.get_rect(centerx = W//2, centery = H//2)

explosion_image = pygame.image.load('image/Explosion.png').convert_alpha()
explosion_image = pygame.transform.scale(explosion_image, (200, 200))
explosion_image_rect = explosion_image.get_rect(centerx = W//2, centery = H//2)

bullet_list = []
bonus_list = []
mine_list = []

class Bullet:
    def __init__(self, image, rect, napr_x, napr_y, shooter):
        self.image = image
        self.rect = rect
        self.napr_x = napr_x
        self.napr_y = napr_y
        self.shooter = shooter
        self.speed = randrange(9, 12)
    def drawing(self):
        sc.blit(self.image, self.rect)
        self.rect.centerx += self.napr_x * self.speed
        self.rect.centery += self.napr_y * self.speed

class Bonus:
    def __init__(self, image, rect, type):
        self.image = image
        self.rect = rect
        self.type = type
        self.shooter = -1
        self.time = 99999999999999999999999999999999999
    def drawing(self):
        sc.blit(self.image, self.rect)
class Mine:
    def __init__(self, image, rect, time):
        self.image = image
        self.rect = rect
        self.time = time
    def drawing(self):
        sc.blit(self.image, self.rect)

speed1 = 4
speed2 = 4
rotationnow = 0
rotationnow2 = 0

LM_1 = 'w'
LM_2 = "w"

global_time = 0
pygame.time.set_timer(pygame.USEREVENT, 100)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            global_time = global_time + 1
            if global_time % 63 == 0:
                REC = bonus_image.get_rect(centerx = randrange(W//5, 4*W//5),
                                            centery = randrange(H//10, 9*H//10))
                type = randrange(0, 2)
                if type == 0:
                    bonus_list.append(Bonus(bonus_image, REC, type))
                elif type == 1:
                    bonus_list.append(Bonus(bonus_image2, REC, type))
                elif type == 2:
                    bonus_list.append(Bonus(bonus_image, REC, 0))
                elif type == 3:
                    bonus_list.append(Bonus(bonus_image, REC, 0))
            elif global_time % 98 == 0:
                REC = mine_image.get_rect(centerx = randrange(W//5, 4*W//5),
                                            centery = randrange(H//10, 9*H//10))
                mine_list.append(Mine(mine_image, REC, global_time))
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE and hp1 > 0:
                REC = bullet_image.get_rect(centerx = hero1_rect.centerx,
                                            centery = hero1_rect.centery,)
        if hp1 > 0 and hp2 > 0:
            if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                REC = bullet_image.get_rect(centerx = hero1_rect.centerx,
                                            centery = hero1_rect.centery,)
                if LM_1 == 'd':
                    bullet_list.append(Bullet(bullet_image, REC, 1, 0, 1))
                elif LM_1 == "a":
                  bullet_list.append(Bullet(bullet_image, REC, -1, 0, 1))
                elif LM_1 == "w":
                    bullet_list.append(Bullet(bullet_image, REC, 0, -1, 1))
                elif LM_1 == "s":
                    bullet_list.append(Bullet(bullet_image, REC, 0, 1, 1))
             elif event.key == pygame.K_RCTRL:
                REC = bullet_image2.get_rect(centerx = hero2_rect.centerx,
                                            centery = hero2_rect.centery,)
                if LM_2 == 'd':
                    bullet_list.append(Bullet(bullet_image2, REC, 1, 0, 0))
                elif LM_2 == "a":
                  bullet_list.append(Bullet(bullet_image2, REC, -1, 0, 0))
                elif LM_2 == "w":
                    bullet_list.append(Bullet(bullet_image2, REC, 0, -1, 0))
                elif LM_2 == "s":
                    bullet_list.append(Bullet(bullet_image2, REC, 0, 1, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        LM_1 = "a"
        if not rotationnow == 240:
            if rotationnow == 90:
                hero1_image = pygame.transform.rotate(hero1_image, -180)
                bullet_image = pygame.transform.rotate(bullet_image, -180)
            if rotationnow == 0:
                hero1_image = pygame.transform.rotate(hero1_image, 90)
                bullet_image = pygame.transform.rotate(bullet_image, 90)
            if rotationnow == 360:
                hero1_image = pygame.transform.rotate(hero1_image, -90)
                bullet_image = pygame.transform.rotate(bullet_image, -90)
            rotationnow = 240
        hero1_rect.centerx -= speed1
    if keys[pygame.K_w]:
        LM_1 = "w"
        if not rotationnow == 0:
            if rotationnow == 90:
                hero1_image = pygame.transform.rotate(hero1_image, 90)
                bullet_image = pygame.transform.rotate(bullet_image, 90)
            if rotationnow == 240:
                hero1_image = pygame.transform.rotate(hero1_image, -90)
                bullet_image = pygame.transform.rotate(bullet_image, -90)
            if rotationnow == 360:
                hero1_image = pygame.transform.rotate(hero1_image, -180)
                bullet_image = pygame.transform.rotate(bullet_image, -180)
            rotationnow = 0
        hero1_rect.centery -= speed1
    if keys[pygame.K_d]:
        LM_1 = "d"
        if not rotationnow == 90:
            if rotationnow == 0:
                hero1_image = pygame.transform.rotate(hero1_image, -90)
                bullet_image = pygame.transform.rotate(bullet_image, -90)
            if rotationnow == 240:
                hero1_image = pygame.transform.rotate(hero1_image, -180)
                bullet_image = pygame.transform.rotate(bullet_image, -180)
            if rotationnow == 360:
                hero1_image = pygame.transform.rotate(hero1_image, 90)
                bullet_image = pygame.transform.rotate(bullet_image, 90)
            rotationnow = 90
        hero1_rect.centerx += speed1
    if keys[pygame.K_s]:
        LM_1 = "s"
        if not rotationnow == 360:
            if rotationnow == 0:
                hero1_image = pygame.transform.rotate(hero1_image, -180)
                bullet_image = pygame.transform.rotate(bullet_image, -180)
            if rotationnow == 240:
                hero1_image = pygame.transform.rotate(hero1_image, 90)
                bullet_image = pygame.transform.rotate(bullet_image, 90)
            if rotationnow == 90:
                hero1_image = pygame.transform.rotate(hero1_image, -90)
                bullet_image = pygame.transform.rotate(bullet_image, -90)
            rotationnow = 360
        hero1_rect.centery += speed1

    if keys[pygame.K_LEFT]:
        LM_2 = "a"
        if not rotationnow2 == 240:
            if rotationnow2 == 90:
                hero2_image = pygame.transform.rotate(hero2_image, -180)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -180)
            if rotationnow2 == 0:
                hero2_image = pygame.transform.rotate(hero2_image, 90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, 90)
            if rotationnow2 == 360:
                hero2_image = pygame.transform.rotate(hero2_image, -90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -90)
            rotationnow2 = 240
        hero2_rect.centerx -= speed2
    if keys[pygame.K_UP]:
        LM_2 = "w"
        if not rotationnow2 == 0:
            if rotationnow2 == 90:
                hero2_image = pygame.transform.rotate(hero2_image, 90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, 90)
            if rotationnow2 == 240:
                hero2_image = pygame.transform.rotate(hero2_image, -90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -90)
            if rotationnow2 == 360:
                hero2_image = pygame.transform.rotate(hero2_image, -180)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -180)
            rotationnow2 = 0
        hero2_rect.centery -= speed2
    if keys[pygame.K_RIGHT]:
        LM_2 = "d"
        if not rotationnow2 == 90:
            if rotationnow2 == 0:
                hero2_image = pygame.transform.rotate(hero2_image, -90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -90)
            if rotationnow2 == 240:
                hero2_image = pygame.transform.rotate(hero2_image, -180)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -180)
            if rotationnow2 == 360:
                hero2_image = pygame.transform.rotate(hero2_image, 90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, 90)
            rotationnow2 = 90
        hero2_rect.centerx += speed2
    if keys[pygame.K_DOWN]:
        LM_2 = "s"
        hero2_rect.centery += speed2
        if not rotationnow2 == 360:
            if rotationnow2 == 0:
                hero2_image = pygame.transform.rotate(hero2_image, -180)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -180)
            if rotationnow2 == 240:
                hero2_image = pygame.transform.rotate(hero2_image, 90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, 90)
            if rotationnow2 == 90:
                hero2_image = pygame.transform.rotate(hero2_image, -90)
                bullet_image2 = pygame.transform.rotate(bullet_image2, -90)
            rotationnow2 = 360
    clock.tick(FPS)
    sc.blit(bg, (0, 0))
    if hero1_rect.centerx + 75 > W:
        hero1_rect.centerx = W - 75
    elif hero1_rect.centerx - 53 < 0:
        hero1_rect.centerx = 0 + 53
    if hero1_rect.centery + 70 > H:
        hero1_rect.centery = H - 70
    elif hero1_rect.centery - 70 < 0:
        hero1_rect.centery = 0 + 70
    if hero2_rect.centerx + 75 > W:
        hero2_rect.centerx = W - 75
    elif hero2_rect.centerx - 53 < 0:
        hero2_rect.centerx = 0 + 53
    if hero2_rect.centery + 70 > H:
        hero2_rect.centery = H - 70
    elif hero2_rect.centery - 70 < 0:
        hero2_rect.centery = 0 + 70
    if hp2 > 0:
        sc.blit(hero2_image, hero2_rect)
    if hp1 > 0:
        sc.blit(hero1_image, hero1_rect)
    if not hp2 > 0 or not hp1 > 0:
        sc.blit(sc_text, (W//3.3, H//3))
    for i in bullet_list:
        i.drawing()
        if i.rect.centerx < -100 or i.rect.centerx > W +100 or\
                i.rect.centery < -100 or i.rect.centery > H +100:

            bullet_list.pop(bullet_list.index(i))
        elif i.rect.colliderect(hero2_rect) and i.shooter == 1:
            bullet_list.pop(bullet_list.index(i))
            hp2 = hp2 - 70
        elif i.rect.colliderect(hero1_rect) and i.shooter == 0:
            bullet_list.pop(bullet_list.index(i))
            hp1 = hp1 - 70
    if hp1 > 0 and hp2 > 0:
        for i in bonus_list:
            i.drawing()
            if i.rect.colliderect(hero1_rect):
                if i.type == 0:
                   hp1 = hp1 + 100
                   if hp1 > 200:
                       hp1 = 200
                elif i.type == 1:
                    i.shooter = 1
                    i.time = global_time
                    speed1 = 6.5
                i.rect.x = 2317823
            elif i.rect.colliderect(hero2_rect):
                if i.type == 0:
                   hp1 = hp1 + 100
                   if hp1 > 200:
                       hp1 = 200
                elif i.type == 1:
                    i.shooter = 2
                    i.time = global_time
                    speed2 = 6.5
                i.rect.x = 2317823
            if global_time - i.time >= 30:
                if i.shooter == 1:
                    speed1 = 4
                elif i.shooter == 2:
                    speed2 = 4
                i.rect.y = 2317823
                i.shooter = -1
                i.time = 99999999999999999999999999999999999
        for i in mine_list:
            i.drawing()
            if i.time + 30 <= global_time:
                i.image = explosion_image
                if i.rect.colliderect(hero1_rect):
                    hp1 = hp1 - 2
                if i.rect.colliderect(hero2_rect):
                    hp2 = hp2 - 2
            if i.time + 40 <= global_time:
                mine_list.pop(mine_list.index(i))
    if hp1 > 0:
        HP_bar = pygame.transform.scale(HP_bar, (hp1, 30))
    else:
        HP_bar = pygame.transform.scale(HP_bar, (0, 0))
    if hp2 > 0:
        HP_bar2 = pygame.transform.scale(HP_bar2, (hp2, 30))
    else:
        HP_bar2 = pygame.transform.scale(HP_bar2, (0, 0))
    sc.blit(healbox, healbox_rect)
    sc.blit(HP_bar, HP_bar_rect)
    sc.blit(healbox2, healbox_rect2)
    sc.blit(HP_bar2, HP_bar_rect2)
    pygame.display.update()
