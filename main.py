import pygame
import ctypes
from ctypes import wintypes 
import keyboard
import time
import threading

def main():
    #https://www.appsloveworld.com/coding/python3x/83/how-to-pin-a-pygame-window-on-top
    pygame.init()
    screen = pygame.display.set_mode((50, 50))
    
    hwnd = pygame.display.get_wm_info()['window']
    
    user32 = ctypes.WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
    user32.SetWindowPos(hwnd, -1, 0, 500, 0, 0, 0x0001)
    

    font = pygame.font.Font('Roboto-Black.ttf', 32)

    number = 0

    def listen():
        sleeptimes = 0.3
        while 1:
            if keyboard.read_key() == "space":
                nonlocal number
                number += 1     
                time.sleep(sleeptimes)
            elif keyboard.read_key() == "r":
                number = 0
            elif keyboard.read_key() == "p":
                quit()
                break

    x = threading.Thread(target=listen)
    x.start()
    while True:

        text = font.render(str(number), True, pygame.color.Color("black"))
        textRect = text.get_rect()
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('grey')
        screen.blit(text, textRect)
        pygame.display.flip()

if __name__ == "__main__":
    main()
