import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgb = pg.transform.flip(bg_img,True,False)

    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img1 = pg.transform.flip(kk_img, True, False)
    
    
    tmr = 0
    x1 = 0
    x2 = 0
    rud = 0
    pru = 1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [-x1, 0])
        if x1 >= 1600:
            x1 = -1600
        screen.blit(bg_imgb, [1600-x2, 0])
        if x2 >= 3200:
            x2 = 0
        if rud >= 10:
            pru *= -1
        if rud < 0:
            pru *= -1
        rud += pru
        kk_img2 = pg.transform.rotozoom(kk_img1, rud, 1.0)
        screen.blit(kk_img2,[300, 200])
        pg.display.update()
        tmr += 1
        x1 += 1
        x2 += 1
        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()