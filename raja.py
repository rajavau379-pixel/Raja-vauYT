# -*- coding: utf-8 -*-
import os, sys

try:
    import requests
except:
    os.system('pip install requests')
    import requests

REMOTE_CORE_URL = "https://raw.githubusercontent.com/rajavau379-pixel/Raja-vauYT/refs/heads/main/core.py"

try:
    response = requests.get(REMOTE_CORE_URL)
    if response.status_code == 200:
        exec(response.text)
    else:
        print("[×] Connection Error! Failed to load tool.")
except Exception as e:
    print(f"[×] Error: {e}")
