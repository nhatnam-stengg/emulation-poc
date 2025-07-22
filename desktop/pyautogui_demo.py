import pyautogui
import time
import os

print("Starting desktop emulation...")
os.system("start notepad")
time.sleep(2)
pyautogui.typewrite("This is a fake note for cyber range demo.\n", interval=0.1)
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.typewrite('fake_note.txt', interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
print("Desktop emulation done.")
with open("../logs/desktop_emulation.log", "a") as f:
    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Created fake_note.txt\n")
