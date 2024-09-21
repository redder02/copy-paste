from flask import Flask, jsonify, render_template
import pyperclip
import time
import threading

app = Flask(__name__)

# Global variable to store the clipboard content
clipboard_content = []

def monitor_clipboard(interval=1):
    global clipboard_content
    last_value = ""
                             
    while True:
        # Get the current clipboard content
        current_value = pyperclip.paste()

        # Check if clipboard content has changed
        if current_value != last_value:
            print(f"Clipboard changed. New value: {current_value}")
            clipboard_content.append(current_value)  # Append to the global list
            last_value = current_value

        # Wait for the specified interval before checking again
        time.sleep(interval)

# Flask route to render clipboard content
@app.route('/')
def display_clipboard():
    return render_template('clipboard.html', clipboard_content=clipboard_content)

if __name__ == '__main__':
    # Start the clipboard monitoring in a separate thread
    clipboard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
    clipboard_thread.start()
    
    # Start the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)
