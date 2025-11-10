import tkinter as tk
from tkinter import filedialog, scrolledtext
import json
from datetime import datetime
import re

# Create the main window
window = tk.Tk()
window.title("LLM API Conversation Viewer")
window.geometry("900x700")  # Width x Height in pixels

# This line keeps the window open until closed
window.mainloop()
