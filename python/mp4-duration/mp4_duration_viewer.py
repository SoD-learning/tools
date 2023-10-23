import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from moviepy.editor import VideoFileClip
import threading


def get_file_durations(folder_path):
    """Scan the folder for mp4 files and retrieve their durations."""
    file_durations = []

    for file in os.listdir(folder_path):
        if file.endswith(".mp4"):
            file_path = os.path.join(folder_path, file)
            try:
                clip = VideoFileClip(file_path)
                duration = round(clip.duration, 2)
                file_durations.append((file, f"{duration} seconds"))
                clip.close()  # Important to release system resources
            except Exception as e:
                messagebox.showerror(
                    "Error", f"An error occurred while processing {file}: {str(e)}"
                )

    return file_durations


def select_folder():
    """Prompt the user to select a folder and process the files within it."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        # Show the progress label
        processing_label.pack()

        # Use a separate thread to process the videos to avoid freezing the GUI
        def process_files():
            file_durations = get_file_durations(folder_path)
            # Insert the data into the treeview
            for file_info in file_durations:
                tree.insert("", tk.END, values=file_info)
            # Hide the progress label
            processing_label.pack_forget()

        processing_thread = threading.Thread(target=process_files)
        processing_thread.start()


# Set up the GUI window
root = tk.Tk()
root.title("MP4 File Duration Viewer")

# Set up the layout
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add a button to allow the user to select a folder
select_button = ttk.Button(frame, text="Select Folder", command=select_folder)
select_button.pack(pady=(0, 10))

# Add a label that will display while processing files
processing_label = ttk.Label(frame, text="Processing files, please wait...")

# Set up the table (treeview) with a scrollbar
tree = ttk.Treeview(frame, columns=("Filename", "Duration"), show="headings")
tree.heading("Filename", text="FILENAME")
tree.heading("Duration", text="DURATION")

# Add a scrollbar
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.configure(yscrollcommand=scrollbar.set)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()
