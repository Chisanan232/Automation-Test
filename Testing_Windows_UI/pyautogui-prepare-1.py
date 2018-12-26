import pyautogui



pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
pyautogui.position()

for i in range(10):
    print('Automatic Test cursor move with coordinate space begin. - ' + str(i) + 'time')
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    print('Automatic Test cursor move with coordinate space end. - ' + str(i) + 'time')

for i in range(10):
    print('Automatic Test cursor move with pixel space begin. - ' + str(i) + 'time')
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
    print('Automatic Test cursor move with pixel space end. - ' + str(i) + 'time')

print('Press Ctrl+C to quit.')



print('Test Finish !')
