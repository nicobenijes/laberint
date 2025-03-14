from pygame import *

#clase padre para objetos
class GameSprite(sprite.Sprite):
   #constructor de clase
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       #cada objeto debe almacenar una propiedad image
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       #cada objeto debe almacenar la propiedad rect – el rectángulo en el cual está inscrito
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#clase derivada para el objeto del jugador (controlado por las flechas)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


#clase heredera para el objeto enemigo (se mueve solo)
class Enemy(GameSprite):
   direction = "izquierda"
   def update(self):
       if self.rect.x <= 470:
           self.direction = "derecha"
       if self.rect.x >= win_width - 85:
           self.direction = "izquierda"


       if self.direction == "izquierda":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed





class wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height

       self.image = Surface((self.width , self.height))
       self.image.fill((color_1, color_2, color_3))

       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))







#Escena del juego:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("LABERINT ZONE")
background = transform.scale(image.load("laberinto.png"), (win_width, win_height))


#Personajes del juego:
player = Player('sonic.png', 5, win_height - 80, 4)
monster = Enemy('eggman.png', win_width - 80, 280, 2)
final = GameSprite('eggman_malo.png', win_width - 120, win_height - 80, 0)


w1 = wall(242, 210, 0, 100, 20, 450, 10)
w2 = wall(242, 210, 0, 100, 480, 350, 10)
w3 = wall(242, 210, 0, 100, 20, 10, 380)
w4 = wall(242, 210, 0, 200, 130, 10, 350)
w5 = wall(242, 210, 0, 450, 130, 10, 360)
w6 = wall(242, 210, 0, 300, 20, 10, 350)
w7 = wall(242, 210, 0, 390, 120, 130, 10)



game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None,70)
win = font.render('¡Ganaste pro!', True, (225, 215, 0))
lose = font.render('¡Perdiste noob!', True, (180, 0, 0))


while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.blit(background,(0, 0))
       player.update()
       monster.update()
      
       player.reset()
       monster.reset()
       final.reset()

       w1.draw_wall()
       w2.draw_wall()
       w3.draw_wall()
       w4.draw_wall()
       w5.draw_wall()
       w6.draw_wall()
       w7.draw_wall()
       


       if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
         finish = True
         window.blit(lose, (200, 200))
         kick.play()

       if sprite.collide_rect(player, final): 
         finish = True
         window.blit(win, (200, 200))
         kick.play()

   display.update()
   clock.tick(FPS)