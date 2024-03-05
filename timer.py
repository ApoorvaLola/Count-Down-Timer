import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        self.label = tk.Label(master, text="Enter time (in seconds):")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()
        
        self.timer_running = False
        
    def start_timer(self):
        if not self.timer_running:
            try:
                self.seconds = int(self.entry.get())
                if self.seconds <= 0:
                    messagebox.showerror("Error", "Please enter a positive integer.")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.")
                return
            
            self.timer_running = True
            self.run_timer()
            
    def run_timer(self):
        while self.seconds > 0:
            self.label.config(text=str(self.seconds))
            self.master.update()
            time.sleep(1)
            self.seconds -= 1
        
        messagebox.showinfo("Timer", "Time's up!")
        self.timer_running = False

def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()