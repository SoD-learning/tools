import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os


def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        # Display the selected file's name
        file_name = os.path.basename(file_path)
        selected_file_label.config(text=f"Selected: {file_name}")

        # Read the PDF file and display the number of pages
        with open(file_path, "rb") as file:
            reader = PdfReader(file)
            total_pages.set(len(reader.pages))  # Update the total_pages variable

        # Update global variable with the file path
        selected_pdf.set(file_path)

        # Enable the "Split PDF" button
        split_pdf_button.config(state=tk.NORMAL)


def split_pdf():
    file_path = selected_pdf.get()
    if not file_path:
        messagebox.showerror("No file", "No file selected for splitting.")
        return

    # Define the save path for the split PDFs
    save_directory = filedialog.askdirectory()
    if not save_directory:
        return

    # Read the PDF file and split it into individual pages
    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        for page_num, page in enumerate(reader.pages):
            output_file_path = os.path.join(save_directory, f"page_{page_num+1}.pdf")
            with open(output_file_path, "wb") as output_file:
                output_file.write(page.getBytes())

    # Show a message box when the splitting is complete
    messagebox.showinfo("Split PDF", "PDF splitting complete.")


def split_pdf_thread(file_path, save_directory, split_every_page, extract_pages_entry):
    status_label.config(text="Splitting PDF...")

    try:
        # Open the source PDF file
        with open(file_path, "rb") as file:
            reader = PdfReader(file)

            if split_every_page:
                # Split every page into a new PDF
                for i in range(len(reader.pages)):
                    writer = PdfWriter()
                    writer.add_page(reader.pages[i])

                    with open(f"{save_directory}/page_{i+1}.pdf", "wb") as new_file:
                        writer.write(new_file)
            elif extract_pages_entry:
                # Extract specific pages
                pages = list(map(int, extract_pages_entry.split("-")))
                writer = PdfWriter()

                for i in range(pages[0] - 1, pages[1]):
                    writer.add_page(reader.pages[i])

                with open(
                    f"{save_directory}/extracted_pages_{pages[0]}_to_{pages[1]}.pdf",
                    "wb",
                ) as new_file:
                    writer.write(new_file)

        status_label.config(text="PDF split successfully.")
    except Exception as e:
        status_label.config(text="An error occurred while splitting the PDF.")
        messagebox.showerror("Splitting error", str(e))
    finally:
        # Re-enable the button
        split_pdf_button.config(state=tk.NORMAL)


# Set up the main application window
app = tk.Tk()
app.title("PDF Splitter")

# Variables to hold user selections and settings
selected_pdf = tk.StringVar()
total_pages = tk.IntVar(value=0)
split_every_page_var = tk.BooleanVar()
extract_pages_var = tk.StringVar()

# Create and place the widgets
title_label = tk.Label(app, text="PDF Splitter", font=("Helvetica", 16, "bold"))
title_label.pack(pady=5)

instructions_label = tk.Label(
    app,
    text="Select a PDF to split it into multiple files or to extract specific pages.",
)
instructions_label.pack(pady=5)

select_pdf_button = tk.Button(app, text="Select PDF", command=select_pdf)
select_pdf_button.pack(pady=10)

selected_file_label = tk.Label(
    app, text="No PDF selected", font=("Helvetica", 10, "italic")
)
selected_file_label.pack(pady=5)

total_pages_label = tk.Label(app, textvariable=total_pages)
total_pages_label.pack(pady=5)

split_every_page_check = tk.Checkbutton(
    app,
    text="Split at every page",
    variable=split_every_page_var,
    onvalue=True,
    offvalue=False,
)
split_every_page_check.pack(pady=5)

extract_pages_label = tk.Label(app, text="Extract pages (e.g., 2-4):")
extract_pages_label.pack(pady=5)

extract_pages_entry = tk.Entry(app, textvariable=extract_pages_var)
extract_pages_entry.pack(pady=5)

split_pdf_button = tk.Button(
    app, text="Split PDF", state=tk.DISABLED, command=split_pdf
)
split_pdf_button.pack(pady=20)

status_label = tk.Label(app, text="")
status_label.pack(pady=5)

# Start the application's main loop
app.mainloop()
