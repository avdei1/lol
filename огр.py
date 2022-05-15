from pygame import *

#music
mixer.init()
mixer.music.load("подлая еврейская музыка.mp3")
mixer.music.play()
#не music
font.init()
font = font.SysFont("Arial", 70)
loos = font.render("БОЖЕ ЧЕЛ КРИНЖ", True, (170,0,85))
#фон
window1 = 900
window2 = 600
window = display.set_mode((window1, window2))
display.set_caption("IGNITE GAME")
ogre = transform.scale(image.load("огрфон.jpg"),(window1, window2))
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True:
            window.blit(ogre, (0, 0))

    display.update()
