import os
import subprocess as sp

paths={
    'notepad':"C:\\Windows\\notepad.exe",
    'discord':"C:\\Users\\avaneeth\\Desktop\\Discord.lnk",
    'telegram':"C:\\Users\\avaneeth\\Desktop\\Telegram.lnk"
    
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_telegram():
    os.startfile(paths['telegram'])


