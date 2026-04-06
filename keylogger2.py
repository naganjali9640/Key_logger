import tkinter as tk
from pynput import keyboard

def on_press(key):
    try:
        display = f"Pressed: {key.char}"
    except AttributeError:
        display = f"Special Key: {key}"
    
    label.config(text=display)

def on_release(key):
    label.config(text="Key Released")

def start_listener():
    global listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    label.config(text="Visualizer Running...")
    start_btn.config(state="disabled")
    stop_btn.config(state="normal")

def stop_listener():
    listener.stop()
    label.config(text="Stopped")
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")

# GUI
root = tk.Tk()
root.title("Key Press Visualizer")
root.geometry("300x200")

label = tk.Label(root, text="Click Start", font=("Arial", 12))
label.pack(pady=20)

start_btn = tk.Button(root, text="Start", command=start_listener)
start_btn.pack(side="left", padx=20)

stop_btn = tk.Button(root, text="Stop", command=stop_listener, state="disabled")
stop_btn.pack(side="right", padx=20)

root.mainloop()
