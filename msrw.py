import tkinter as tk
import pyautogui
import random
import time
import threading
import sys
import os
from pynput import keyboard


# -- Resource path for the file --
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

running = False

# --- Main program (window) ---
app_window = tk.Tk()
app_window.title("MS RW")

def start_application():
    global running
    running = not running
    if running:
        start_button.config(text="Stop")
        threading.Thread(target=farmer).start()
    else:
        start_button.config(text="Run")

# --- The main program ---
def farmer():
    global running
    while running:
        lines = open(resource_path('szavak.txt')).read().splitlines()
        szo = random.choice(lines)
        pyautogui.moveTo(298, 138)  # klikk a keresőre
        time.sleep(0.2)
        pyautogui.click()

        time.sleep(1.5)
        pyautogui.write(szo)

        time.sleep(1.25)
        pyautogui.moveTo(229, 131)  # nagyító kereső
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(3)

        pyautogui.moveTo(298, 138)  # klikk a keresőre
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(1.25)

        pyautogui.moveTo(1300, 143)  # klikk az x-re
        time.sleep(1)
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(897, 138)  # klikk az x-re
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)

# --- Function for listener ---
def on_press(key):
    if key == keyboard.Key.f10:
        start_application()

# --- The toggle button / tip label ---
tip_label = tk.Label(app_window, text="Tip: F10 for toggle on/off")
tip_label.pack()

start_button = tk.Button(app_window, text="Run", command=start_application)
start_button.pack()

# --- App settings ---
app_window.geometry("200x60")
app_window.resizable(False, False)

# --- Listen to the keyboard event ---
listener = keyboard.Listener(on_press=on_press)
listener.start()

# --- Run the application ---
app_window.mainloop()
