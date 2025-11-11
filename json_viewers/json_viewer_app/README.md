# LLM Conversation Viewer - Standalone Desktop Application

A native macOS desktop application for viewing JSON conversation exports from LLM API applications in a clean, readable format.

## Features

- **Native macOS Application**: Double-click to launch, no command line needed
- **Clean Interface**: Easy-to-read conversation display with proper formatting
- **Model Identification**: Shows which AI model generated each response
- **Timestamps**: Displays when each message was sent in human-readable format
- **Markdown Stripping**: Removes markdown artifacts for cleaner reading
- **Light Theme**: Comfortable light gray background with dark text

## System Requirements

- macOS (developed and tested on macOS Tahoe 26.1 with M2 chip)
- Python 3.11+ (for building from source)

## Installation

### Option 1: Use Pre-built App (Recommended)

1. Download `JSON Viewer.app`
2. Move it to your Applications folder
3. Double-click to launch

### Option 2: Build from Source

#### Prerequisites
```bash
# Install pyenv (if not already installed)
brew install pyenv

# Install tcl-tk@8 for Tkinter support
brew install tcl-tk@8
brew link tcl-tk@8 --force

# Configure environment
export LDFLAGS="-L/opt/homebrew/opt/tcl-tk@8/lib"
export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk@8/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/tcl-tk@8/lib/pkgconfig"

# Install Python 3.11.7 with Tkinter
pyenv install 3.11.7
pyenv global 3.11.7
```

#### Building the App
```bash
# Install py2app
pip install py2app

# Build the application
python setup.py py2app

# The app will be created in dist/JSON Viewer.app
# Move it to Applications
mv "dist/JSON Viewer.app" /Applications/
```

#### Rebuilding After Changes
```bash
# Clean previous builds
rm -rf build dist

# Rebuild
python setup.py py2app
```

## Usage

1. Launch the application from Applications folder or Spotlight
2. Click **File → Open JSON File**
3. Select your JSON conversation export
4. View the formatted conversation

### Supported JSON Format

The viewer expects JSON files with this structure:
```json
{
  "conversation": [
    {
      "role": "user" | "assistant",
      "content": "Message content",
      "modelName": "Model Name (optional)",
      "timestamp": 1234567890123
    }
  ]
}
```

## Development

This project was developed with assistance from Claude Sonnet 4.5 (Anthropic).

### Project Structure
```
json_viewer_app/
├── json_viewer_app.py    # Main application code
├── setup.py              # py2app configuration
├── app_icon.icns         # Application icon
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

### Testing During Development

For faster iteration during development, use alias mode:
```bash
python setup.py py2app -A
```

To see error messages while testing:
```bash
"dist/JSON Viewer.app/Contents/MacOS/JSON Viewer"
```

## Version History

- **v0.1.0** (MVP) - Initial release with basic conversation viewing

## Roadmap / TODO

### Planned Features

- [ ] **Markdown Rendering**: Display formatted markdown instead of stripping it
- [ ] **Search Functionality**: Search within conversations for specific text
- [ ] **Model Filtering**: Filter messages by specific AI models
- [ ] **Export Options**: Export conversations to PDF, HTML, or plain text
- [ ] **Dark Mode**: Toggle between light and dark themes
- [ ] **Multiple File Tabs**: Open and switch between multiple conversations
- [ ] **Statistics Dashboard**: Show conversation metrics (message count, model usage, etc.)
- [ ] **Conversation Comparison**: Side-by-side view of multiple conversations
- [ ] **Keyboard Shortcuts**: Quick navigation and actions
- [ ] **Recent Files Menu**: Quick access to recently opened conversations
- [ ] **Auto-reload**: Watch file for changes and auto-refresh
- [ ] **Syntax Highlighting**: Color-code different message types and models
- [ ] **Copy/Share**: Easy copying of individual messages or entire conversations
- [ ] **Preferences Panel**: Customize font size, colors, and display options

### Nice-to-Have Features

- [ ] **JSON Validation**: Check and report JSON structure issues before loading
- [ ] **Drag-and-Drop**: Drag JSON files onto app icon or window to open
- [ ] **Custom Themes**: User-defined color schemes
- [ ] **Conversation Bookmarks**: Mark important messages for quick reference
- [ ] **Message Threading**: Collapse/expand conversation branches

## Known Issues

- On first launch after building, you may need to run the app from terminal once before it launches normally from Finder

## License

Free to use and modify as needed.

## Contributing

This is a personal utility project. Feel free to fork and adapt for your own needs.
