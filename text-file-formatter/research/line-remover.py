import tkinter as tk
from tkinter import filedialog


def process_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

        processed_lines = []

        for line in lines:
            line = line.strip()  # Remove leading and trailing whitespace
            if line:
                processed_lines.append(line)

        # Combine lines and add spaces after each word
        processed_text = " ".join(processed_lines)

        # Write the processed content to the output file
        with open(output_file, "w") as file:
            file.write(processed_text)

        print("File processed successfully.")

    except FileNotFoundError:
        print("Input file not found.")


def browse_input_file():
    input_file_path = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file_path)


def browse_output_file():
    output_file_path = filedialog.asksaveasfilename()
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file_path)


def process_files():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    process_file(input_file, output_file)


# Create the main application window
root = tk.Tk()
root.title("Line Break Remover")

# Create and place widgets
tk.Label(root, text="Input File:").pack(pady=5)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.pack(pady=5)
tk.Button(root, text="Browse", command=browse_input_file).pack(pady=5)

tk.Label(root, text="Output File:").pack(pady=5)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.pack(pady=5)
tk.Button(root, text="Browse", command=browse_output_file).pack(pady=5)

tk.Button(root, text="Process", command=process_files).pack(pady=20)

# Run the main event loop
root.mainloop()
