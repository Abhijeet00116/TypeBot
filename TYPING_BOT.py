from distutils.command.config import LANG_EXT
from pynput.keyboard import Key, Controller, Listener
from pynput import mouse
import time
import pyscreenshot
import pytesseract as pt

def on_click(x,y,button, pressed):
    if pressed:
        on_click.px = x
        on_click.py = y
    else:
        on_click.rx = x
        on_click.ry = y
    if not pressed:
        return False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()


img = pyscreenshot.grab(bbox=(on_click.px, on_click.py, on_click.rx, on_click.ry))
txt = str(pt.image_to_string(img,lang='eng'))
print(txt)

keyboard = Controller()
def on_press(key):
    if key == Key.num_lock:
        for i in txt:
            keyboard.press(i)
            keyboard.release(i)
            time.sleep(0.01)



with Listener(on_press=on_press) as listener:
    listener.join()
