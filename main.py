import keyboard as k
import time
from pathlib import Path

selfPath = Path.cwd()
image_path = str(selfPath) + "\\bg_image\\anonymous.jpg"

print(image_path)


def time_between_action():
    time.sleep(1)


def end_cmd():
    k.press_and_release('alt+F4')


k.press_and_release('windows+r')

time_between_action()
k.write("cmd")
k.press_and_release("enter")

time_between_action()
k.write(f"reg add \"HKEY_CURRENT_USER\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d {image_path}")
k.press_and_release("enter")
time_between_action()
k.write("yes")
k.press_and_release("enter")

time_between_action()
k.write("RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True")
k.press_and_release("enter")

time_between_action()
end_cmd()
