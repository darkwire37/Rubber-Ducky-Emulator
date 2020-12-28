import pyautogui as pag
import time
import sys
args = sys.argv
if len(args) != 2:
    print("Please specify the file path of the script you would like to run.")
    quit()

script = open(sys.argv[1])

lines = script.readlines()

for line in lines: 
    print(line)
    command = line.split(None, 1)[0].lower()
    try:
        parameter = line.split(None, 1)[1].strip().lower()
    except IndexError:
        pass
    if command == "control":
        command = "ctrl"
    if parameter == "control":
        parameter = "ctrl"

        
    if command == "string":
        pag.typewrite(parameter, interval=0.1)

    elif command == "delay":
        time.sleep(int(parameter)/1000)

    elif command == "enter":
        pag.typewrite(['enter'], interval=0.1)
    elif command == "gui":
        pag.hotkey('winleft',parameter)
    elif command == "rem":
        pass

    else:
        pag.hotkey(command, parameter)
