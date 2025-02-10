from pygame import *
from random import *
options = (1400,1000)
init()
mixer.init()

finish = False

wind = display.set_mode(options)
clock_ = time.Clock()
background = transform.scale(image.load('ping_pong_arena.jpg'),options) 

font.init()
font_ = font.Font(None,100)
lose = font_.render('YOU LOSE!',True,(255,0,0))



game = True

class game_objects (sprite.Sprite):
    def __init__(self,picture,x,y,width,length,speed=0):
        super().__init__()
        self.image = transform.scale(image.load(picture),(width,length))
        self.rect = self.image.get_rect()
        self.rect.x = x  
        self.rect.y = y
        self.speed = speed
    def reset (self):
        wind.blit(self.image,(self.rect.x,self.rect.y))

class raketka_0(game_objects):
    def update (self):
        if ball_object.rect.x >= 950:
            if ball_object.rect.y > self.rect.y + 100:
                self.rect.y += self.speed
            if ball_object.rect.y < self.rect.y + 100:
                self.rect.y -= self.speed            

        # keys = key.get_pressed()
        # if keys[K_UP] and self.rect.y >= 0:
        #     self.rect.y -= self.speed
        # if keys[K_DOWN] and self.rect.y <= 800:
        #     self.rect.y += self.speed
        
    
        
class raketka_1(game_objects):
    def update (self):
  
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 800:
            self.rect.y += self.speed



class ball(game_objects):
    def __init__(self, picture, x, y, width, length, speed=0,speed_y=0):
        super().__init__(picture, x, y, width, length, speed)
        self.speed_y = speed_y
    def update (self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y

raketka_0_object = raketka_0('raketka.jpg',1300,500,50,200,3.7)
raketka_1_object = raketka_1('raketka.jpg',50,500,50,200,5)

speed_ball_x = choice([-5,5])
speed_ball_y = choice([-5,5])
print(speed_ball_x)
print(speed_ball_y )
ball_object = ball('ball.jpg',700,500,50,50,speed_ball_x,speed_ball_y)
while game :
    
    for i in event.get():
        if i.type == QUIT:
            game = False
    if not finish :
        wind.blit(background,(0,0))
        raketka_0_object.update()
        raketka_1_object.update()    
        ball_object.update()

        if ball_object.rect.x >= 1350 or ball_object.rect.x <= 0 :
            wind.blit(lose,(500,400))
            finish = True


        if ball_object.rect.y >= 950 or ball_object.rect.y <= 0 :
            ball_object.speed_y *= -1

        if sprite.collide_rect(raketka_0_object,ball_object)  or sprite.collide_rect(raketka_1_object,ball_object) :
            ball_object.speed *= -1



        
        ball_object.reset()
        raketka_0_object.reset()
        raketka_1_object.reset()
    display.update()
    clock_.tick(60)
    print('(˘･_･˘)')