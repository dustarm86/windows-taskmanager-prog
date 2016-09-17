import subprocess

# runs windows shell command to open task manager and change priority for .exe file to high
subprocess.call('wmic process where name="Overwatch.exe" CALL setpriority 128', shell=True)

"""
Priority Integers:

idle: 64

below normal: 16384

normal: 32

above normal: 32768

high priority: 128

real time: 256
"""
