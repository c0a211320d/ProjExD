import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

def check_bound(rct, scr_rct):
    bmimg_sfc = pg.Surface((20, 20))
    yoko, tate, = +1, +1
    if rct.left < scr_rct.left or scr_rct.right < rct.right:
        yoko = -1
        pg.draw.circle(bmimg_sfc, (0, 255, 0), (10, 10), 10)
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:
        pg.draw.circle(bmimg_sfc, (0, 0, 255), (10, 10), 10)
        tate = -1
    return yoko, tate

def main():
    clock  = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))  #Surface
    screen_rct = screen_sfc.get_rect()   #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    #pg.display.update()
    #clock.tick(0.5)

    #こうかとん
    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

    #爆弾
    bmimg_sfc = pg.Surface((20, 20))   #Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_states = pg.key.get_pressed()   #辞書
        if key_states[pg.K_UP] == True:
            kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True:
            kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True:
            kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:
            kkimg_rct.centerx += 1
        if check_bound(kkimg_rct, screen_rct) != (1,1):
            if key_states[pg.K_UP] == True:
                kkimg_rct.centery += 1
            if key_states[pg.K_DOWN] == True:
                kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT] == True:
                kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True:
                kkimg_rct.center -= 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        bmimg_rct.move_ip(vx, vy)
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate
        if kkimg_rct.colliderect(bmimg_rct):
            tkm.showerror("報告", "ぶつかったので爆発しました")
            return
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()   
    main()
    pg.quit()
    
    sys.exit()
    