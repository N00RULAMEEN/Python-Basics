import os
import time

folder = r"C:\Users\Admin\Desktop\Tor Browser\n\PROGRAMMING\Python milan"
os.chdir(folder)

while True:
    os.system("git add .")
    os.system('git commit -m "Auto daily update"')
    os.system("git push")
    time.sleep(86400)  # wait for 1 day
