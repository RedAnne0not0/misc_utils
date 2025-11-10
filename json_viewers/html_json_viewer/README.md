# LLM API Conversation Viewer

A simple, standalone HTML viewer for displaying JSON conversation exports from LLM API applications in a clean, readable format.
Designed for use with the [My API Chat application](https://github.com/mbbrinkman/my_api_chat) from [Michael Brinkman](https://github.com/mbbrinkman)

## Features

- **Markdown Rendering**: Properly displays formatted text including headers, lists, bold/italic text, and code blocks
- **Model Identification**: Shows which AI model generated each response
- **Timestamps**: Displays when each message was sent
- **Clean Interface**: Chat-style layout with color-coded user and assistant messages
- **No Installation Required**: Single HTML file that runs entirely in your browser
- **Drag-and-Drop Ready**: Simple file upload interface

## Usage

1. Download or clone `json_viewer.html`
2. Open the file in any modern web browser (Chrome, Firefox, Safari, Edge)
3. Click the upload area and select your JSON conversation file
4. View your formatted conversation

## JSON Format

This viewer expects JSON files with the following structure:
```json
{
  "conversation": [
    {
      "role": "user" | "assistant",
      "content": "Message content (supports markdown)",
      "modelName": "Model Name (optional)",
      "timestamp": 1234567890123
    }
  ]
}
```

## Supported Features

- User and assistant messages with distinct styling
- Multiple AI models in a single conversation
- Markdown formatting in message content
- Model name prefixes (e.g., `[Model Name]: content`)
- Unix timestamp conversion to readable dates

## Technical Details

- Intended for use with the json files exported from [Michael Brinkman's API Chat application](https://github.com/mbbrinkman/my_api_chat)
- **Dependencies**: Uses [marked.js](https://marked.js.org/) CDN for markdown parsing
- **Browser Compatibility**: Works in all modern browsers (no server required)
- **File Processing**: Uses JavaScript FileReader API for client-side file reading
- **Privacy**: All processing happens locally in your browser - no data is sent to any server

## Development

This project was created with assistance from Claude Sonnet 4.5 (Anthropic).

## License

Free to use and modify as needed.

## Future Enhancements

Potential features for future versions:
- Search/filter functionality
- Export to other formats (PDF, HTML)
- Collapsible message threads
- Dark mode
- Model-specific color coding
- Statistics dashboard (message count, model usage, etc.)
