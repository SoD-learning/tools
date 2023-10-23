import tkinter as tk
from tkinter import filedialog


def remove_extra_line_breaks(input_text):
    # Remove extra line breaks
    lines = input_text.split("\n")
    processed_lines = [line.strip() for line in lines if line.strip()]
    return " ".join(processed_lines)


def handle_special_characters(input_text):
    # Define the standard characters (letters, numbers, common punctuation,
    # spaces, and line breaks)
    standard_chars = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789.,!?;:()-‘’'\"\n "
    )

    # Identify non-standard characters and add a line break before them
    output_text = "".join(
        "\n" + char if char not in standard_chars else char for char in input_text
    )
    return output_text


def process_text(input_text, format_headings):
    lines = input_text.split("\n")
    formatted_text = []

    for line in lines:
        words = line.split()
        new_line = []

        for word in words:
            if format_headings and word.isupper() and word.endswith(":"):
                new_line.append("\n\n" + word)
            elif format_headings and word[:-1].isupper() and word[-1] == ":":
                new_line.append("\n" + word[:-1] + ":")
            else:
                new_line.append(word)

        formatted_text.append(" ".join(new_line))

    return "\n".join(formatted_text)


def process_files():
    input_file_path = filedialog.askopenfilename(title="Select Text File")
    output_file_path = filedialog.asksaveasfilename(title="Save Processed File As")

    if input_file_path and output_file_path:
        with open(input_file_path, "r", encoding="utf-8") as file:
            input_text = file.read()

        format_headings = format_headings_var.get()

        if remove_line_breaks_var.get() and handle_special_chars_var.get():
            # Remove line breaks first and then handle special characters
            output_text = handle_special_characters(
                remove_extra_line_breaks(input_text)
            )
        elif remove_line_breaks_var.get():
            output_text = remove_extra_line_breaks(input_text)
        elif handle_special_chars_var.get():
            output_text = handle_special_characters(input_text)
        else:
            output_text = input_text

        output_text = process_text(output_text, format_headings)

        with open(output_file_path, "w", encoding="utf-8") as file:
            file.write(output_text)

        output_label.config(text="File processed and saved successfully.")


# Create the main application window
root = tk.Tk()
root.title("Text File Formatter")

# Checkbox for removing extra line breaks
remove_line_breaks_var = tk.IntVar()
remove_line_breaks_checkbox = tk.Checkbutton(
    root, text="Remove extra line breaks", variable=remove_line_breaks_var
)
remove_line_breaks_checkbox.pack(pady=5)

# Checkbox for handling special characters
handle_special_chars_var = tk.IntVar()
handle_special_chars_checkbox = tk.Checkbutton(
    root, text="Handle special characters", variable=handle_special_chars_var
)
handle_special_chars_checkbox.pack(pady=5)

# Checkbox for formatting headings
format_headings_var = tk.IntVar()
format_headings_checkbox = tk.Checkbutton(
    root, text="Format headings", variable=format_headings_var
)
format_headings_checkbox.pack(pady=5)

# Create and place the "Process File" button
process_button = tk.Button(root, text="Process File", command=process_files)
process_button.pack(pady=20)

# Label to display status
output_label = tk.Label(root, text="")
output_label.pack()

# Run the main event loop
root.mainloop()
