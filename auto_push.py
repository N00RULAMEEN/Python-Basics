import os
import time
import subprocess

# -------------------------
# 1. SET YOUR PROJECT PATH
# -------------------------
FOLDER = r"C:\Users\Admin\Desktop\Tor Browser\n\Programming\Python-Milan"

# -------------------------
# 2. Change directory
# -------------------------
if not os.path.exists(FOLDER):
    print(f"Error: Folder does not exist → {FOLDER}")
    exit()

os.chdir(FOLDER)
print(f"Working in: {os.getcwd()}")

# -------------------------
# 3. Check if Git repo
# -------------------------
if not os.path.exists(".git"):
    print("This folder is NOT a Git repository.")
    print("Run: git init")
    exit()

# -------------------------
# 4. Auto push loop
# -------------------------
while True:
    print("\n--------------------------------------")
    print("🔄 Running Auto Git Push...")
    print("--------------------------------------")

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto daily update"], check=False)
        subprocess.run(["git", "push"], check=False)

    except Exception as e:
        print("❌ Error occurred:", e)

    print("✅ Waiting 5 minutes before next push...")
    time.sleep(300)  # 300 seconds = 5 minutes
