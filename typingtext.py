import time
import pyautogui

def type_text(text, interval=0.1):
    """
    Types out the given text with the specified typing interval.
    
    Parameters:
        text (str): The text to be typed out.
        interval (float): The interval between each keystroke.
    """
    time.sleep(5)  # This gives you some time to switch to the text input field
    pyautogui.typewrite(text, interval=interval)

# Example usage:
text_to_type = "Hello, this is an automated typing test."
type_text(text_to_type)
#