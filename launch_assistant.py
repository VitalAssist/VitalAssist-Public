<<<<<<< HEAD
import subprocess
import webbrowser
import os
import time
import threading

import subprocess, webbrowser, os, time, threading

HTML_PORT = 8000
API_PORT  = 5000
BROWSER_URL = f"http://localhost:{HTML_PORT}/index.html"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_web_server():
    subprocess.Popen(
        ["python", "-m", "http.server", str(HTML_PORT)],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def run_voice_server():
    subprocess.Popen(
        ["python", "vitalassist_web_server.py"],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def open_browser():
    time.sleep(2)
    webbrowser.open(BROWSER_URL)

if __name__ == "__main__":
    print("🚀 Launching VitalAssist…")
    threading.Thread(target=run_web_server).start()
    threading.Thread(target=run_voice_server).start()
    threading.Thread(target=open_browser).start()
    print("🧠 VitalAssist is now running. Press Ctrl+C to exit.")

    print(f"🌐 Visit: {BROWSER_URL}")
    print("Press Ctrl+C to exit.")
=======
import subprocess
import webbrowser
import os
import time
import threading

import subprocess, webbrowser, os, time, threading

HTML_PORT = 8000
API_PORT  = 5000
BROWSER_URL = f"http://localhost:{HTML_PORT}/index.html"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_web_server():
    subprocess.Popen(
        ["python", "-m", "http.server", str(HTML_PORT)],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def run_voice_server():
    subprocess.Popen(
        ["python", "vitalassist_web_server.py"],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def open_browser():
    time.sleep(2)
    webbrowser.open(BROWSER_URL)

if __name__ == "__main__":
    print("🚀 Launching VitalAssist…")
    threading.Thread(target=run_web_server).start()
    threading.Thread(target=run_voice_server).start()
    threading.Thread(target=open_browser).start()
    print("🧠 VitalAssist is now running. Press Ctrl+C to exit.")

    print(f"🌐 Visit: {BROWSER_URL}")
    print("Press Ctrl+C to exit.")
>>>>>>> 7cb058c207c6b6ed161b514703ee245b665d0829
