# 3D Donut Animation in Terminal

This project animates a 3D donut shape in the terminal using Python. It also includes a script to resize the terminal window for optimal viewing of the animation.

## Files

1. `donut.py`: This script animates a 3D donut shape on the terminal. It uses 3D math to calculate pixel coordinates and shading for each frame of a rotating donut surface. The z-buffer and character output arrays animate it on the terminal one frame at a time.

2. `resize.py`: This script resizes a Windows PowerShell or cmd window on the desktop. It uses pyautogui to find and resize an open command window, providing a consistent window size each time.

3. `main.py`: This script runs the `donut.py` and `resize.py` scripts concurrently in separate threads. It uses subprocess to execute them and threading to run them asynchronously.

## How to Run

1. Ensure you have Python installed on your machine.

2. Install the required Python packages by running `pip install pyautogui` in your terminal.

3. Run the `main.py` script by typing `python main.py` in your terminal.

## Note

- The `resize.py` script is designed to work with Windows PowerShell or cmd windows. If you're using a different terminal, you may need to modify this script for it to work correctly.

- The `donut.py` script uses the terminal size to calculate the donut's position and size. If your terminal window is too small or big, you may not see the full animation.

