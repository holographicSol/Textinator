import os
import time
import win32com.client
from pywinauto import application

app = application.Application()
shell = win32com.client.Dispatch("WScript.Shell")

var_0 = ''


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def funk_0():
    global var_0
    print('-- time remaining: 3 second')
    time.sleep(1)
    print('-- time remaining: 2 second')
    time.sleep(1)
    print('-- time remaining: 1 second')
    time.sleep(1)
    shell.SendKeys(var_0)


while True:
    clear_console()
    print('-'*100)
    print(' '*44 + 'TEXTINATOR')
    print('\nCircumvents password input limitations where input may be restricted.')
    print('\nUpon hitting enter you will have 3 seconds to select the text field in which to output data.')
    var_0 = input('\nEnter text to output:')
    funk_0()
