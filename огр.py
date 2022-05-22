from pygame import *
#music===========================================================================================================
mixer.init()
mixer.music.load("подлая еврейская музыка.mp3")
mixer.music.play()
#не music========================================================================================================
font.init()
font = font.SysFont("Arial", 70)
loos = font.render("БОЖЕ ЧЕЛ КРИНЖ", True, (144,33,85))
#фон=============================================================================================================
window1 = 900
window2 = 600
window = display.set_mode((window1, window2))
display.set_caption("IGNITE GAME")
ogre = transform.scale(image.load("огрфон.jpg"),(window1, window2))
game = True
finish = False
#класс гаме спрайте==============================================================================================
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс игрока1===================================================================================================
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= 10
        if keys_pressed[K_s]:
            self.rect.y += 10
#класс игрока2===================================================================================================
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_p]:
            self.rect.y -= 10
        if keys_pressed[K_l]:
            self.rect.y += 10
#спрайтики=======================================================================================================
dubina1 = Player1("дубина1.png", 20, 400, 15, 80, 200)
dubina2 = Player2("дубина2.png", 800, 400, 1150, 80, 200)
ignite = GameSprite("игнайт.jpg", 410, 400, 582, 60, 60)
#оаоаоаоаоаоаоаоа================================================================================================
speed_x = 3
speed_y = 3
#цикл============================================================================================================
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(ogre, (0, 0))
        ignite.rect.x += speed_x
        ignite.rect.y += speed_y
        if ignite.rect.y > window2-50 or ignite.rect.y < 0:
                speed_y *= -1
        if sprite.collide_rect(dubina1, ignite) or sprite.collide_rect(dubina2, ignite):
            speed_x *= -1
        if ignite.rect.x <0:
            finish = True
            window.blit(loos , (200, 200))
        if ignite.rect.x >window1:
            finish = True
            window.blit(loos , (250, 350))
        dubina1.update()
        dubina1.reset()
        dubina2.update()
        dubina2.reset()
        ignite.update()
        ignite.reset()
    display.update()
