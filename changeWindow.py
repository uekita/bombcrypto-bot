from cv2 import cv2
import pyautogui
import sys

acc_1_img = cv2.imread('targets/accounts/acc_1.png')
acc_2_img = cv2.imread('targets/accounts/acc_2.png')

def changeWindow(atempt):
    pyautogui.keyDown('alt')
    for x in range(atempt):
        pyautogui.press('tab')    
    pyautogui.keyUp('alt')

def goToAccount(num):
    atempt = 0
    while True:
        if (checkAcc(num) == True):
            return
        else:
            changeWindow(atempt)
            atempt = atempt + 1

def checkAcc(num):
    name = 'acc_' + str(num) + '_img'
    if (pyautogui.locateOnScreen(globals()[name], confidence =.8) is not None):
        sys.stdout.write('\nFound Account ' + str(num))
        return True
    else:
        return False