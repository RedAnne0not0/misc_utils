import tkinter as tk
from tkinter import filedialog, scrolledtext
import json
from datetime import datetime
import re

# Create the main window
window = tk.Tk()
window.title("LLM API Conversation Viewer")
window.geometry("900x700")  # Width x Height in pixels

# Create a scrolled text widget to display the conversation
text_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,  # Wrap text at word boundaries
    width=100,
    height=40,
    font=("Arial", 11),
    padx=10,
    pady=10
)
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Make it read-only (user can't edit it)
text_area.config(state=tk.DISABLED)

# This line keeps the window open until closed
window.mainloop()
