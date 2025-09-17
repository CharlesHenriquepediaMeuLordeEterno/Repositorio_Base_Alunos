import pyautogui, mouseinfo, time


mouseinfo.mouseInfo()

pyautogui.moveTo(671,1056, duration=1)
pyautogui.leftClick()
pyautogui.moveTo(1810,0, duration=5)
pyautogui.click()
pyautogui.moveTo(170,56, duration=3)
pyautogui.write("youtube.com")
pyautogui.press("Enter")
pyautogui.sleep(10)
pyautogui.moveTo(766,104, duration=2)
pyautogui.leftClick()
pyautogui.write("neymar jr skills")
pyautogui.press("Enter")
pyautogui.leftClick(686,630, duration=3)
pyautogui.moveTo(1866,618,duration=3)
pyautogui.leftClick()