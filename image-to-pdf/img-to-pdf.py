import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from fpdf import FPDF
import threading
import os


def select_files():
    files = filedialog.askopenfilenames(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if files:
        listbox_files.delete(0, tk.END)  # Clear the current list
        for file in files:
            filename = os.path.basename(file)  # Extract only the file's name
            listbox_files.insert(tk.END, filename)  # Add file to the listbox
        convert_button.config(state=tk.NORMAL)  # Enable the convert button
        status_label.config(text="Files selected. Ready to convert.")


def create_pdf_thread(
    files, save_path, current_task_label, status_label, spinner_canvas
):
    pdf = FPDF()

    # Start the spinner (make it visible)
    spinner_canvas.pack(pady=5)

    # Process each image
    for index, image_file in enumerate(files, 1):
        current_task_label.config(
            text=f"Processing image {index}/{len(files)}..."
        )  # Update current task
        with Image.open(image_file) as img:
            width, height = img.size
            new_size = calculate_pdf_image_size(width, height)

            pdf.add_page()
            pdf.image(image_file, 0, 0, new_size[0], new_size[1])

    pdf.output(save_path)
    current_task_label.config(text="")  # Clear the current task
    status_label.config(text=f"Conversion successful. PDF saved to {save_path}")

    # Stop the spinner (make it invisible)
    spinner_canvas.pack_forget()


def create_pdf():
    files = listbox_files.get(0, tk.END)
    if not files:
        messagebox.showwarning("No selection", "No files selected for conversion.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
    )
    if not save_path:
        status_label.config(text="Conversion canceled.")
        return

    status_label.config(text="Conversion started...")

    # Start PDF conversion in a separate thread so the UI doesn't freeze
    conversion_thread = threading.Thread(
        target=create_pdf_thread,
        args=(files, save_path, current_task_label, status_label, spinner_canvas),
        daemon=True,
    )
    conversion_thread.start()


def calculate_pdf_image_size(image_width, image_height, max_pdf_page_size=(210, 297)):
    width_ratio = max_pdf_page_size[0] / image_width
    height_ratio = max_pdf_page_size[1] / image_height
    scale_ratio = min(width_ratio, height_ratio)

    return (scale_ratio * image_width, scale_ratio * image_height)


def spinner(canvas, angle):
    # Clear the current canvas
    canvas.delete("all")

    # Create arc (a part of a circle) as the spinner with increased width
    canvas.create_arc(
        5, 5, 25, 25, start=angle, extent=300, style=tk.ARC, outline="black", width=5
    )  # Increased line thickness

    # Update the angle
    angle = (angle + 5) % 360

    # Call the spinner function again after 50ms with the new angle
    canvas.after(50, lambda: spinner(canvas, angle))


# Set up the main application window
app = tk.Tk()
app.title("Image to PDF Converter")

# Create a title label to the application
title_label = tk.Label(app, text="Image to PDF", font=("Helvetica", 16, "bold"))
title_label.pack(pady=5)

# Create instructions for the user
instructions_label_1 = tk.Label(
    app,
    text="1. Click the `Select Images` button and choose the images you want to convert.",
    wraplength=400,
)
instructions_label_1.pack(pady=5)

instructions_label_2 = tk.Label(
    app,
    text="2. Click the 'Convert to PDF' button to start the process. Depending on the image sizes, it may take some time to complete.",
    wraplength=400,
)
instructions_label_2.pack(pady=5)

# Create a frame for the listbox and scrollbar
frame_files = tk.Frame(app)
frame_files.pack(pady=10)  # fill=tk.X makes the frame fill the window horizontally

# Create a listbox to display the selected files
listbox_files = tk.Listbox(
    frame_files, width=50, height=10, selectmode=tk.EXTENDED
)  # Reduced width
listbox_files.pack(
    side=tk.LEFT, fill=tk.BOTH, expand=True
)  # fill and expand make the listbox fill the frame

# Create a scrollbar for the listbox
scrollbar_files = tk.Scrollbar(frame_files)
scrollbar_files.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar and listbox
listbox_files.config(yscrollcommand=scrollbar_files.set)
scrollbar_files.config(command=listbox_files.yview)

# Create a button to select files
select_button = tk.Button(app, text="Select Images", command=select_files)
select_button.pack(pady=10)

# Create a button to convert files, initially disabled
convert_button = tk.Button(
    app, text="Convert to PDF", command=create_pdf, state=tk.DISABLED
)
convert_button.pack(pady=10)

# Create a label for global status updates
status_label = tk.Label(
    app, text="Please select images to convert.", font=("Helvetica", 10, "bold")
)
status_label.pack(pady=5)

# Create a label for displaying the current task (e.g., which file is being processed)
current_task_label = tk.Label(app, text="", font=("Helvetica", 10))
current_task_label.pack(pady=5)

# Create a canvas for the spinner and start the spinner function
spinner_canvas = tk.Canvas(
    app, width=30, height=30, bg=app.cget("bg"), highlightthickness=0
)  # Removed background
spinner_canvas.pack(pady=5)
spinner_canvas.pack_forget()  # Initially, the spinner is not visible
spinner_thread = threading.Thread(target=spinner, args=(spinner_canvas, 0), daemon=True)
spinner_thread.start()

# Determine the longest message and set the window width based on it
longest_message = "Conversion successful. PDF saved to C:/Users/Username/long/path/to/your/new/file.pdf"
estimated_font_size = 8  # The average size (in pixels) of a character in the font used (this is an estimation and might need adjustment)
padding = 40  # Additional space to accommodate paddings, borders, etc.

# Calculate the window width: the length of the message in characters multiplied by the size of a character, plus padding
window_width = len(longest_message) * estimated_font_size + padding

app.geometry(
    f"{window_width}x500"
)  # Adjusting the window's size; height is kept the same for consistency

app.mainloop()
