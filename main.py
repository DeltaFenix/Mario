from pygame import *
v0 = 0
class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
    def move(self, v0):
        if self.rect.x <= 0 and self.x_speed < 0:
            self.x_speed = 0
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0: 
            for p0 in platforms_touched:
                self.rect.right = min(self.rect.right, p0.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if v0 < 0: 
            for p1 in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p1.rect.top)
        

       
v = 10
window = display.set_mode((1280, 720))
back = (51, 133, 45)
window.fill(back)
picture1 = image.load('mario_back2.jpg')
picture1 = transform.scale(picture1, (1280, 720))
display.set_caption('mario.png')
wall1 = GameSprite('mario_wall.png', 75, 200, 300, 400)
wall2 = GameSprite('mario_wall.png', 75, 250, 700, 350)
wall3 = GameSprite('mario_wall.png', 75, 300, 1000, 300)
player1 = Player('mario.png', 75, 75, 50, 525 , 0)
player2 = Player('turtle.png', 75, 75, 400, 525, -5)
player3 = Player('enemy.png', 75, 75, 800, 525, -5)
player4 = Player('enemy.png', 75, 75, 900, 525, -5)
fin_pic = image.load('finish.jpg')
enemy = sprite.Group()
enemy.add(player2)
enemy.add(player3)
enemy.add(player4)
fin_pic = transform.scale(fin_pic, (50, 500))
walls = sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
display.update()
fin = GameSprite('finish.jpg', 50, 500, 1200, 90)
run = True
lose = False
win = False
lose_pic = transform.scale(image.load('fail_1.jpg'), (1280, 720))
win_pic = transform.scale(image.load('winner_1.jpg'), (1280, 720))
while run:
    v0 = 0
    time.delay(0)
    window.blit(picture1, (0, 0))
    wall1.reset()
    wall2.reset()
    wall3.reset()

    fin.reset()
    player1.reset()
    player2.reset()
    player3.reset()
    player4.reset()
    for e in event.get():
        q = e
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if player1.rect.y == 525 or sprite.spritecollide(player1, walls, False):
                    v0 = 400
            elif e.key == K_RIGHT:
                player1.x_speed = v
            elif e.key == K_LEFT:
                player1.x_speed = -v
        elif e.type == KEYUP:
            if e.key == K_RIGHT:
                player1.x_speed = 0
            elif e.key == K_LEFT:
                player1.x_speed = 0
    for f in event.get():
        if f != q:
            if e.type == QUIT:
                run = False
            elif f.type == KEYDOWN:
                if f.key == K_SPACE:
                    if player1.rect.y == 525 or sprite.spritecollide(player1, walls, False):
                        v0 = 350
                elif f.key == K_RIGHT:
                    player1.x_speed = v
                elif f.key == K_LEFT:
                    player1.x_speed = -v
            elif f.type == KEYUP:
                if f.key == K_RIGHT:
                    player1.x_speed = 0
                elif f.key == K_LEFT:
                    player1.x_speed = 0
    a = player1.rect.y
    player1.move(v0)
    player2.rect.x += player2.x_speed
    player3.rect.x += player3.x_speed
    player4.rect.x += player4.x_speed

    player1.rect.y -= v0
    if player1.rect.y >= 525:
        v0 = 0
    else:
        player1.rect.y += 50
    b = player1.rect.y
    if sprite.spritecollide(player2, walls, False):
        player2.x_speed = -player2.x_speed
    elif sprite.spritecollide(player3, walls, False):
        player3.x_speed = -player3.x_speed
    elif sprite.spritecollide(player4, walls, False):
        player4.x_speed = -player4.x_speed
    if sprite.collide_rect(player1, player2) and a<b:
        player2.kill()
        player2.rect.y = 1000
    elif sprite.collide_rect(player1, player3) and a<b:
        player3.kill()
        player3.rect.y = 1000
    elif sprite.collide_rect(player1, player4):
        player4.kill()
        player4.rect.y = 1000
    if v0 == 0 and sprite.collide_rect(player1, wall1) and player1.rect.y < 525:
        player1.rect.bottom = min(player1.rect.bottom, wall1.rect.top)
    elif v0 == 0 and sprite.collide_rect(player1, wall2) and player1.rect.y < 525:
        player1.rect.bottom = min(player1.rect.bottom, wall2.rect.top)
    elif v0 == 0 and sprite.collide_rect(player1, wall3) and player1.rect.y < 525:
        player1.rect.bottom = min(player1.rect.bottom, wall3.rect.top)
    if sprite.spritecollide(player1, enemy, False) and a >= b:
        lose = True
    if sprite.collide_rect(player1, fin):
        win = True
    if lose == True:
        window.blit(lose_pic, (0, 0))
    elif win == True:
        window.blit(win_pic, (0, 0))
    display.update()
