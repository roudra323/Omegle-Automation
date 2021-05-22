import pyautogui as pg
pg.PAUSE = 5


def msg():
    pg.write("Stand With Palestine")
    pg.PAUSE = 1

    pg.press('enter')


for i in range(10):
    try:
        pg.PAUSE = 5
        msg()

        for i in range(3):
            pg.press('esc')
            pg.PAUSE = 2
    except:
        pg.press('esc')
