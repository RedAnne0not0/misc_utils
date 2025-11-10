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
    font=("Arial", 14),
    padx=10,
    pady=10,
    bg="#f5f5f5",  # Light gray background
    fg="#333333",  # Dark gray text
    insertbackground="#333333"  # Cursor color
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
            try:
                # Read and parse the JSON file
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Display the conversation
                display_conversation(data)
                
            except json.JSONDecodeError:
                text_area.config(state=tk.NORMAL)
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, "Error: Invalid JSON file")
                text_area.config(state=tk.DISABLED)
            except Exception as e:
                text_area.config(state=tk.NORMAL)
                text_area.delete(1.0, tk.END)
                text_area.insert(1.0, f"Error: {str(e)}")
                text_area.config(state=tk.DISABLED)

# Function to remove markdown formatting
def strip_markdown(text):
    # Remove headers (### text)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    
    # Remove bold (**text** or __text__)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'__(.+?)__', r'\1', text)
    
    # Remove italic (*text* or _text_)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'_(.+?)_', r'\1', text)
    
    # Remove inline code (`text`)
    text = re.sub(r'`(.+?)`', r'\1', text)
    
    # Remove code blocks (```text```)
    text = re.sub(r'```[\s\S]*?```', '[code block]', text)
    
    return text

# Function to display the conversation
def display_conversation(data):
    # Enable editing temporarily
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)  # Clear existing text
    
    # Check if data has the expected structure
    if 'conversation' not in data:
        text_area.insert(tk.END, "Error: JSON file doesn't have 'conversation' field")
        text_area.config(state=tk.DISABLED)
        return
    
    # Loop through each message
    for message in data['conversation']:
        role = message.get('role', 'unknown')
        content = message.get('content', '')
        model_name = message.get('modelName', '')
        timestamp = message.get('timestamp', None)
        
        # Format the message header
        if role == 'user':
            text_area.insert(tk.END, "=" * 80 + "\n")
            text_area.insert(tk.END, "USER\n")
        else:  # assistant
            text_area.insert(tk.END, "=" * 80 + "\n")
            if model_name:
                text_area.insert(tk.END, f"ASSISTANT ({model_name})\n")
            else:
                text_area.insert(tk.END, "ASSISTANT\n")
        
        # Add timestamp if available
        if timestamp:
            dt = datetime.fromtimestamp(timestamp / 1000)  # Convert from milliseconds
            text_area.insert(tk.END, f"Time: {dt.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        text_area.insert(tk.END, "-" * 80 + "\n")
        
        # Remove model name prefix if it exists (e.g., "[xAI: Grok 4 Fast]: ")
        cleaned_content = content
        model_prefix_match = re.match(r'^\[([^\]]+)\]:\s*', cleaned_content)
        if model_prefix_match:
            cleaned_content = cleaned_content[len(model_prefix_match.group(0)):]

        # Clean and display the content
        cleaned_content = strip_markdown(cleaned_content)
        text_area.insert(tk.END, cleaned_content + "\n\n")   

    # Make read-only again
    text_area.config(state=tk.DISABLED)
    
    # Scroll to top
    text_area.see(1.0)

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
