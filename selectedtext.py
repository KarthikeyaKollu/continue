import time
import pyautogui
import pyperclip

def get_selected_text():
    # Simulate Ctrl+C to copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)  # Wait briefly for copying to complete
    return pyperclip.paste()

def monitor_selection():
    previous_position = pyautogui.position()
    previous_text = ''
    
    while True:
        current_position = pyautogui.position()
        print(current_position)
        if current_position != previous_position:
            selected_text = get_selected_text()
            if selected_text != previous_text:
                print("Selected text:", selected_text)
                previous_text = selected_text
        
        previous_position = current_position
        time.sleep(0.1)  # Check mouse position every 0.1 seconds

monitor_selection()
