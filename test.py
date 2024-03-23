import pyperclip
import time

def prompt_inquiry(selected_text):
    # Display an input box to prompt for an inquiry
    inquiry = input(f"Inquiry for selected text '{selected_text}': ")
    print("Inquiry:", inquiry)
    # Process the inquiry and selected text here

def main():
    previous_selection = ""

    while True:
        # Get currently selected text
        selected_text = pyperclip.paste()

        # Check if selection has changed
        if selected_text and selected_text != previous_selection:
            previous_selection = selected_text
            prompt_inquiry(selected_text)

        # Pause briefly before checking again
        time.sleep(0.5)

if __name__ == "__main__":
    main()
