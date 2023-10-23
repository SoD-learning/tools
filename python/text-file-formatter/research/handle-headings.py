import tkinter as tk
from tkinter import filedialog


def process_text(input_text):
    lines = input_text.split("\n")
    formatted_text = []

    for line in lines:
        words = line.split()
        new_line = []

        for word in words:
            if word.isupper() and word.endswith(":"):
                new_line.append("\n\n" + word)
            elif word[:-1].isupper() and word[-1] == ":":
                new_line.append("\n" + word[:-1] + ":")
            else:
                new_line.append(word)

        formatted_text.append(" ".join(new_line))

    return "\n".join(formatted_text)


def format_text():
    input_text = text_input.get("1.0", tk.END)
    formatted_text = process_text(input_text)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, formatted_text)


def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            input_text = file.read()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, input_text)


def save_to_file():
    formatted_text = text_output.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(formatted_text)


# Create the GUI
root = tk.Tk()
root.title("Text Formatter")

# Input text area
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=10)

# Load from file button
load_button = tk.Button(root, text="Load Text from File", command=browse_file)
load_button.pack()

# Process button
process_button = tk.Button(root, text="Process Text", command=format_text)
process_button.pack()

# Output text area
text_output = tk.Text(root, height=10, width=50)
text_output.pack(pady=10)

# Save to file button
save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack()

root.mainloop()
