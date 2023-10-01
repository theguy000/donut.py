import subprocess
import time
from threading import Thread

def run_script(script):
    subprocess.call(["python", script])

def main():
    Thread(target=run_script, args=("donut.py",)).start()
    time.sleep(2)
    Thread(target=run_script, args=("resize.py",)).start()

if __name__ == "__main__":
    main()