import time
import win32com.client
from pywinauto import application

app = application.Application()
shell = win32com.client.Dispatch("WScript.Shell")

var_0 = ''


def funk_0():
    global var_0

    time.sleep(3)
    shell.SendKeys(var_0)


while True:
    print('-'*200)
    print('TEXTINATOR circumvents many input limitations in password fields and other sensitive input fields where input may be restricted.')
    print('')
    print('Upon hitting enter you will have 3 seconds to select the text field in which to output data.')
    var_0 = input('\nenter text to output:')
    funk_0()

