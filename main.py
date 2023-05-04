from ppy.cli import main

import os
import shutil
import winreg
import ctypes
import sys

FOLDER_CMD = "ppython_basic_wk"
sys.stdout.reconfigure(encoding="utf-8")


def is_path_ppy():
    # check is file
    if os.path.isdir(f"C:\{FOLDER_CMD}"):
        return True
    else:
        return False


def copy_to_drive_c():
    # copy file ppy.exe to C:\FOLDER_CMD if not has folder FOLDER_CMD then create it
    if not is_path_ppy():
        os.mkdir(f"C:\{FOLDER_CMD}")
    if is_path_ppy():
        shutil.copy("dist/ppy.exe", f"C:\{FOLDER_CMD}\ppy.exe")


def add_path_ppy():
    """
    add path ppython_basic_wk to environment variable system path
    """
    new_path = rf"C:\{FOLDER_CMD}"

    key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        "System\\CurrentControlSet\\Control\\Session Manager\\Environment",
        0,
        winreg.KEY_ALL_ACCESS,
    )

    path_value, _ = winreg.QueryValueEx(key, "PATH")

    new_path_value = f"{path_value};{new_path}"

    winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value)

    os.environ["PATH"] = new_path_value

    winreg.CloseKey(key)


if is_path_ppy():
    copy_to_drive_c()
    add_path_ppy()
else:
    main()
