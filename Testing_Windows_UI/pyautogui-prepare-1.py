from unittest import TestCase
import pyautogui
import unittest


class TestWindowsGUI(TestCase):
    def gui_test_1(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        width, height = pyautogui.size()
        print('Screen width: ', width)
        print('Screen height: ', height)
        pyautogui.position()

        for i in range(10):
            print('Automatic Test cursor move with coordinate space begin. - ' + str(i + 1) + ' time')
            pyautogui.moveTo(100, 100, duration=0.25)
            pyautogui.moveTo(200, 100, duration=0.25)
            pyautogui.moveTo(200, 200, duration=0.25)
            pyautogui.moveTo(100, 200, duration=0.25)
            print('Automatic Test cursor move with coordinate space end. - ' + str(i + 1) + ' time')

        for i in range(10):
            print('Automatic Test cursor move with pixel space begin. - ' + str(i + 1) + ' time')
            pyautogui.moveRel(100, 0, duration=0.25)
            pyautogui.moveRel(0, 100, duration=0.25)
            pyautogui.moveRel(-100, 0, duration=0.25)
            pyautogui.moveRel(0, -100, duration=0.25)
            print('Automatic Test cursor move with pixel space end. - ' + str(i + 1) + ' time')

        print('Press Ctrl+C to quit.')

    def gui_test_2(self):
        try:
            while True:
                x, y = pyautogui.position()
                position_str = 'X:' + str(x).rjust(4) + 'Y:' + str(y).rjust(4)
                pix = pyautogui.screenshot().getpixel((x, y))
                position_str += 'RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'
                print(position_str, end='')
                print('\b'*len(position_str), end='', flush=True)
        except KeyboardInterrupt as e:
            print('Error: ', e)

    def test_main_test(self):
        self.gui_test_2()
        print('Test Finish !')


if __name__ == '__main__':
    print('Automatic Test Start.')
    unittest.main()
