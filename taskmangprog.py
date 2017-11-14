import subprocess

# runs windows command prompt command to force teamviewer to close
subprocess.call('Taskkill /IM TeamViewer.exe /F')

# runs windows compant prompt command to open Destiny 2's .exe shortcut
subprocess.call('C:\Users\Dustin\Desktop\Destiny2')

# wait 10 secs for battle.net launcher to close
time.sleep(10)

# re-open destiny 2 shortcut after battle.net has closed
subprocess.call('C:\Users\Dustin\Desktop\Destiny2')

# wait 5 secs before changing destiny's task manager priority to high
time.sleep(5)

# runs windows command prompt command to open task manager and change priority for .exe file to high
subprocess.call('wmic process where name="Destiny2.exe" CALL setpriority 128', shell=True)

"""
Priority Integers:

idle: 64

below normal: 16384

normal: 32

above normal: 32768

high priority: 128

real time: 256
"""
