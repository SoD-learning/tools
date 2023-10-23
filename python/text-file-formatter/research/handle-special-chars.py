import tkinter as tk
from tkinter import filedialog


def process_file():
    input_file_path = filedialog.askopenfilename(title="Select Text File")
    output_file_path = filedialog.asksaveasfilename(title="Save Processed File As")

    # Define the standard characters (letters, numbers, common punctuation,
    # spaces, and line breaks)
    standard_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?;:()-'\"\n "
    )

    if input_file_path and output_file_path:
        with open(input_file_path, "r", encoding="utf-8") as file:
            input_text = file.read()

        # Identify non-standard characters and add a line break before them
        output_text = "".join(
            "\n" + char if char not in standard_chars else char for char in input_text
        )

        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(output_text)

        output_label.config(text="File processed and saved successfully.")


# Create the main application window
root = tk.Tk()
root.title("Special Character Line Breaker")

# Create and place the "Process File" button
process_button = tk.Button(root, text="Process File", command=process_file)
process_button.pack(pady=20)

# Label to display status
output_label = tk.Label(root, text="")
output_label.pack()

# Run the main event loop
root.mainloop()
