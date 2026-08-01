import os
import time
import sys
import platform
import pynput

idle_mins = 15
idle_secs = idle_mins * 60

last_click = time.time()

def reset_timer(*args):
    global last_click
    last_click = time.time()

def shutdown(*args):
    ops = platform.system().lower()

    if 'windows' in ops:
        os.system('shutdown /s /t 1')
    elif 'linux' in ops:
        os.system('sudo shutdown -h now')
    elif 'darwin' in ops:
        os.system('sudo shutdown -h now')
    else:
        pass

mouse = pynput.mouse.Listener(on_move=reset_timer, on_click=reset_timer, on_scroll=reset_timer)
keyboard = pynput.keyboard.Listener(on_press=reset_timer)

try:
    while True:
        idle_time = time.time() - last_click
        if idle_time > idle_secs:
            shutdown()
            break
        time.sleep(1)
finally:
    mouse.stop()
    keyboard.stop()
