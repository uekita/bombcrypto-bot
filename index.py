from cv2 import cv2
import fnmatch
import numpy as np
import mss
import os
import pyautogui
import time
import sys

import changeWindow
import yaml

cat = """
                                                _
                                                \`*-.
                                                 )  _`-.
                                                .  : `. .
                                                : _   '  \\
                                                ; *` _.   `*-._
                                                `-.-'          `-.
                                                  ;       `       `.
                                                  :.       .        \\
                                                  . \  .   :   .-'   .
                                                  '  `+.;  ;  '      :
                                                  :  '  |    ;       ;-.
                                                  ; '   : :`-:     _.`* ;
                                               .*' /  .*' ; .*`- +'  `*'
                                               `*-*   `*-*  `*-*'
====== Please, consider buying me an coffe :) =========================
==== 0xbd06182D8360FB7AC1B05e871e56c76372510dDf =======================
==== https://www.paypal.com/donate?hosted_button_id=JVYSC6ZYCNQQQ =====
=======================================================================

>>---> Press ctrl + c to kill the bot.
>>---> Some configs can be fount in the config.yaml file.
"""

print(cat)

if __name__ == '__main__':
    stream = open("config.yaml", 'r')
    c = yaml.safe_load(stream)
ct = c['trashhold']

pyautogui.PAUSE = c['time_intervals']['interval_between_moviments']

pyautogui.FAILSAFE = True
hero_clicks = 0
login_attempts = 0
num_of_acoounts = len(fnmatch.filter(os.listdir('targets/accounts'), '*.png'))

# var images
go_work_img = cv2.imread('targets/go-work.png')
commom_img = cv2.imread('targets/commom-text.png')
arrow_img = cv2.imread('targets/go-back-arrow.png')
hero_img = cv2.imread('targets/hero-icon.png')
x_button_img = cv2.imread('targets/x.png')
teasureHunt_icon_img = cv2.imread('targets/treasure-hunt-icon.png')
ok_btn_img = cv2.imread('targets/ok.png')
connect_wallet_btn_img = cv2.imread('targets/connect-wallet.png')
select_wallet_img = cv2.imread('targets/select-wallet.png')
select_wallet_hover_img = cv2.imread('targets/select-wallet-1-hover.png')
select_metamask_no_hover_img = cv2.imread('targets/select-wallet-1-no-hover.png')
sign_btn_img = cv2.imread('targets/select-wallet-2.png')
new_map_btn_img = cv2.imread('targets/new-map.png')
green_bar = cv2.imread('targets/green-bar.png')
refresh_img = cv2.imread('targets/refresh_1.png')
empty_cache_hard_reload_img = cv2.imread('targets/empty_cache_hard_reload2.png')
error_header_img = cv2.imread("targets/error_header.png")
chest_img = cv2.imread("targets/chest_img.png")
top_left_img = cv2.imread("targets/top_left.png")
home_heroes_img = cv2.imread("targets/home_heroes.png")
coin_img = cv2.imread("targets/coin.png")
acc_1_img = cv2.imread('targets/accounts/acc_1.png')
acc_2_img = cv2.imread('targets/accounts/acc_2.png')

def dot():
    sys.stdout.write(".")
    sys.stdout.flush()

def clickBtn(img,name=None, timeout=3, trashhold = ct['default'], button='left'):
    dot()
    if not name is None:
        pass
    start = time.time()
    clicked = False
    while(not clicked):
        # im = pyautogui.screenshot(region = (0, 0, 300, 400))
        matches = positions(img, trashhold=trashhold)
        if(len(matches)==0):
            hast_timed_out = time.time()-start > timeout
            if(hast_timed_out):
                if not name is None:
                    pass
                    # print('timed out')
                return False
            # print('button not found yet')
            continue

        x,y,w,h = matches[0]
        pyautogui.moveTo(x+w/2,y+h/2,1)
        print('\nmoved to {}'.format(name))
        if button=='left':
            pyautogui.click()
        elif button=='right':
            pyautogui.click(button='right')
        return True

def printSreen():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}

        # Grab the data
        #sct_img = np.array(sct.grab(monitor))
        sct_img = np.array(sct.grab(sct.monitors[0]))
        return sct_img[:,:,:3]

def positions(target, trashhold=ct['default']):
    img = printSreen()
    result = cv2.matchTemplate(img,target,cv2.TM_CCORR_NORMED)
    w = target.shape[1]
    h = target.shape[0]

    yloc, xloc = np.where(result >= trashhold)


    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def scroll():

    commoms = positions(commom_img, trashhold = ct['commom'])
    if (len(commoms) == 0):
        # print('no commom text found')
        return
    x,y,w,h = commoms[len(commoms)-1]
    # print('moving to {},{} and scrolling'.format(x,y))
#
    pyautogui.moveTo(x,y,1)

    if not c['use_click_and_drag_instead_of_scroll']:
        pyautogui.scroll(-c['scroll_size'])
    else:
        pyautogui.dragRel(0,-c['click_and_drag_amount'],duration=1)


def clickButtons():
    buttons = positions(go_work_img, trashhold=ct['go_to_work_btn'])
    # print('buttons: {}'.format(len(buttons)))
    for (x, y, w, h) in buttons:
        pyautogui.moveTo(x+(w/2),y+(h/2),1)
        pyautogui.click()
        global hero_clicks
        hero_clicks = hero_clicks + 1
        #cv2.rectangle(sct_img, (x, y) , (x + w, y + h), (0,255,255),2)
    return len(buttons)

def isWorking(bar, buttons):
    y = bar[1]

    for (_,button_y,_,button_h) in buttons:
        isBelow = y < (button_y + button_h)
        isAbove = y > (button_y - button_h)
        if isBelow and isAbove:
            return False
    return True
    
def hardReload():
    sys.stdout.write('\nTrying to Hard reload.')
    pyautogui.press('f12')
    clickBtn(refresh_img, name='refresh_bhtton', timeout=10, button='right')
    clickBtn(empty_cache_hard_reload_img, name='empty_cache_hard_reload_button', timeout=10)
    pyautogui.press('f12')

def clickGreenBarButtons():
    # ele clicka nos q tao trabaiano mas axo q n importa
    offset = 130
    green_bars = positions(green_bar, trashhold=ct['green_bar'])
    buttons = positions(go_work_img, trashhold=ct['go_to_work_btn'])

    not_working_green_bars = []
    for bar in green_bars:
        if not isWorking(bar, buttons):
            not_working_green_bars.append(bar)
    if len(not_working_green_bars) > 0:
        sys.stdout.write('\nclicking in %d heroes.' % len(not_working_green_bars))

    # se tiver botao com y maior que bar y-10 e menor que y+10
    for (x, y, w, h) in not_working_green_bars:
        # isWorking(y, buttons)
        pyautogui.moveTo(x+offset+(w/2),y+(h/2),1)
        pyautogui.click()
        global hero_clicks
        hero_clicks = hero_clicks + 1
        #cv2.rectangle(sct_img, (x, y) , (x + w, y + h), (0,255,255),2)
    return len(not_working_green_bars)


def goToHeroes():
    if clickBtn(arrow_img):
        global login_attempts
        login_attempts = 0

    # time.sleep(5)
    clickBtn(hero_img)
    # time.sleep(5)
    # validate if heroes is loaded
    for x in range(15):
        sys.stdout.write('\nCheck if herores has loaded')
        if (pyautogui.locateOnScreen(home_heroes_img, confidence =.8) is not None):
            return   
        time.sleep(1)
    

def goToGame():
    clickBtn(x_button_img)
    clickBtn(teasureHunt_icon_img)

def refreshHeroesPositions():
    clickBtn(arrow_img)
    clickBtn(teasureHunt_icon_img)
    # time.sleep(3)
    clickBtn(teasureHunt_icon_img)

def login():
    global login_attempts
    if (pyautogui.locateOnScreen(chest_img, confidence =.8) is not None):
        sys.stdout.write('\nGame is logged in')
        return
    
    if login_attempts > 3:
       sys.stdout.write('\ntoo many login attempts, refreshing.')
       login_attempts = 0
       hardReload()
       return

    if clickBtn(connect_wallet_btn_img, name='connectWalletBtn', timeout = 10):
        sys.stdout.write('\nConnect wallet button detected, logging in!')
        #TODO mto ele da erro e poco o botao n abre
        # time.sleep(10)
        
    if clickBtn(select_wallet_img, name='selectWalletBtn', timeout = 10):
            sys.stdout.write('\nSelecting wallet!')
        #TODO mto ele da erro e poco o botao n abre
        # time.sleep(10)

    if clickBtn(sign_btn_img, name='sign button', timeout=8):
        # sometimes the sign popup appears imediately
        login_attempts = login_attempts + 1
        # print('sign button clicked')
        # print('{} login attempt'.format(login_attempts))
        # time.sleep(5)
        #if clickBtn(teasureHunt_icon_img, name='teasureHunt', timeout = 15):
            # print('sucessfully login, treasure hunt btn clicked')
         #   login_attempts = 0
        # time.sleep(15)
        return
        # click ok button

    if not clickBtn(select_metamask_no_hover_img, name='selectMetamaskBtn'):
        if clickBtn(select_wallet_hover_img, name='selectMetamaskHoverBtn', trashhold = ct['select_wallet_buttons'] ):
            pass
            # o ideal era que ele alternasse entre checar cada um dos 2 por um tempo 
            # print('sleep in case there is no metamask text removed')
            # time.sleep(20)
    else:
        pass
        # print('sleep in case there is no metamask text removed')
        # time.sleep(20)

    if clickBtn(sign_btn_img, name='signBtn', timeout = 20):
        login_attempts = login_attempts + 1
        # print('sign button clicked')
        # print('{} login attempt'.format(login_attempts))
        # time.sleep(25)
        if clickBtn(teasureHunt_icon_img, name='teasureHunt', timeout=25):
            # print('sucessfully login, treasure hunt btn clicked')
            login_attempts = 0
        # time.sleep(15)

    if clickBtn(ok_btn_img, name='okBtn', timeout=5):
        pass
        # time.sleep(15)
        # print('ok button clicked')

    # checks for login errors for 60 sec
    for x in range(60):
        sys.stdout.write('\nCheck if login has errors')
        if (pyautogui.locateOnScreen(error_header_img, confidence =.8) is not None):
            sys.stdout.write('\nConnection error detected!')
            login()
        if (pyautogui.locateOnScreen(chest_img, confidence =.8) is not None):
            sys.stdout.write('\nSuccessful login!')
            return    
        time.sleep(1)
    return

def simulateMove():
    clickBtn(top_left_img)
    clickBtn(coin_img)

def refreshHeroes():
    goToHeroes()
    if c['only_click_heroes_with_green_bar']:
        print('\nSending heroes with an green stamina bar to work!')
    else:
        sys.stdout.write('\nSending all heroes to work!')
    buttonsClicked = 1
    empty_scrolls_attempts = 2
    while(empty_scrolls_attempts >0):
        if c['only_click_heroes_with_green_bar']:
            buttonsClicked = clickGreenBarButtons()
        else:
            buttonsClicked = clickButtons()
        if buttonsClicked == 0:
            empty_scrolls_attempts = empty_scrolls_attempts - 1
            # print('no buttons found after scrolling, trying {} more times'.format(empty_scrolls_attempts))
        # !mudei scroll pra baixo
        scroll()
        time.sleep(2)
    sys.stdout.write('\n{} heroes sent to work so far'.format(hero_clicks))
    goToGame()

def main():
    time.sleep(5)
    t = c['time_intervals']
    lasts = []
    for x in range(num_of_acoounts):
        lasts.append({
            "login" : 0,
            "heroes" : 0,
            "new_map" : 0,
            "refresh_heroes" : 0
        })

    while True:
        for x in range(num_of_acoounts):
            changeWindow.goToAccount(x + 1)
            
            now = time.time()

            if now - lasts[x]["login"] > t['check_for_login'] * 60:
                sys.stdout.write("\nChecking if game has disconnected.")
                sys.stdout.flush()
                lasts[x]["login"] = now
                login()
                sys.stdout.write("\n")
            else:
                simulateMove()
            
            if now - lasts[x]["heroes"] > t['send_heroes_for_work'] * 60:
                lasts[x]["heroes"] = now
                sys.stdout.write('\nSending heroes to work.')
                refreshHeroes()
                sys.stdout.write("\n")

            if now - lasts[x]["new_map"] > t['check_for_new_map_button']:
                lasts[x]["new_map"] = now
                if clickBtn(new_map_btn_img):
                    with open('new-map.log','a') as new_map_log:
                        new_map_log.write(str(time.time())+'\n')
                    sys.stdout.write('\nNew Map button clicked!\n')

            if now - lasts[x]["refresh_heroes"] > t['refresh_heroes_positions'] * 60 :
                lasts[x]["refresh_heroes"] = now
                sys.stdout.write('\nRefreshing Heroes Positions.\n')
                refreshHeroesPositions()

            #clickBtn(teasureHunt)
            sys.stdout.write(".")
            sys.stdout.flush()

            time.sleep(1)


main()



#cv2.imshow('img',sct_img)
#cv2.waitKey()

# chacar se tem o sign antes de aperta o connect wallet ?
# arrumar aquela parte do codigo copiado onde tem q checar o sign 2 vezes ?
# colocar o botao em pt
# melhorar o log
# salvar timestamp dos clickes em newmap em um arquivo
# soh resetar posiçoes se n tiver clickado em newmap em x segundos

# pegar o offset dinamicamente
# clickar so no q nao tao trabalhando pra evitar um loop infinito no final do scroll se ainda tiver um verdinho
