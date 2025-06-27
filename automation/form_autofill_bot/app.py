import pyautogui
import time

time.sleep(10)

pyautogui.click(x=453, y=603)  
pyautogui.write("Sirasit Boonklang", interval=0.1)

pyautogui.click(x=453, y=770) 
pyautogui.write("90", interval=0.1)

pyautogui.click(x=453, y=938)  
pyautogui.press("down", presses=1)  
pyautogui.press("enter")

pyautogui.click(x=453, y=1111)  
pyautogui.write("7", interval=0.1)

pyautogui.click(x=434, y=1196)  

pyautogui.click(x=666, y=1265)  

print("Form submitted automatically!")
