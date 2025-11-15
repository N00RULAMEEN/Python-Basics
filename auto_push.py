import os
import time

folder = r"C:\Users\Admin\Desktop\Tor Browser\n\Programming\Python-Milan"
os.chdir(folder)

while True:
    os.system("git add .")
    os.system('git commit -m "Auto daily update"')
    os.system("git push")
    time.sleep(500)  # wait for 5 minutes
