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

# Function that will run when user clicks "Open File"
def open_file():
    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select JSON file",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    
    if file_path:
        # For now, just display the file path
        text_area.config(state=tk.NORMAL)  # Enable editing temporarily
        text_area.delete(1.0, tk.END)  # Clear existing text
        text_area.insert(1.0, f"Opened: {file_path}\n\nWe'll load the conversation here next!")
        text_area.config(state=tk.DISABLED)  # Make read-only again

# Create menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open JSON File", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# This line keeps the window open until closed
window.mainloop()
