import re

URL = input("URL : ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)", URL, re.IGNORECASE):
    print(f"UserName: ", matches.group(1))