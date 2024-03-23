import tkinter as tk
import pyperclip
import time

def prompt_inquiry(selected_text):
    # Create a Tkinter window for the input box
    inquiry_window = tk.Tk()
    inquiry_window.title("Inquiry")
    # inquiry_window.overrideredirect(True)

    # Make the window slightly transparent
    inquiry_window.attributes('-alpha', 0.9)

    # Position the window in the center of the screen
    window_width = 300
    window_height = 40
    screen_width = inquiry_window.winfo_screenwidth()
    screen_height = inquiry_window.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    inquiry_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create a larger entry widget with white background and black text
    entry_font = ("Arial", 20)
    inquiry_entry = tk.Entry(inquiry_window, width=50, highlightthickness=0, bg="black", fg="white", font=entry_font,
                              borderwidth=0, relief=tk.FLAT)  # Set borderwidth and relief
    inquiry_entry.pack(padx=5, pady=2, fill=tk.BOTH, expand=True)  # Fill the entire space
    

    # Function to process the inquiry (when Enter is pressed)
    def process_inquiry(event=None):
        inquiry = inquiry_entry.get()
        print("Inquiry:", inquiry)
        inquiry_window.destroy()  
        inquiry_window.update()  # Force the update

    # Bind the <Return> key to submit the inquiry
    inquiry_entry.bind('<Return>', process_inquiry)

    # Focus the entry widget
    inquiry_entry.focus()

    # Run the Tkinter event loop
    inquiry_window.mainloop()

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
