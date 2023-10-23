# MP4 File Duration Viewer

## Contents

- [Description for Developers](#developer-description)
- [Description for Non-Developers](#non-developer-description)

## Developer Description 👨‍💻

### Project Overview:

The primary objective of this script is to provide a graphical user interface for scanning a selected directory for MP4 files and displaying the duration of each file. It employs the `moviepy` library to extract video durations and `tkinter` for the graphical user interface.

### Technology Used

- Python
- Tkinter
- MoviePy
- Threading

### File Structure:

- `mp4_duration_viewer.py`: The main and only file in this utility.

### Usage:

1. Ensure you have Python installed on your machine.
2. Install the required libraries by running `pip install moviepy`.
3. Run `python mp4_duration_viewer.py` in your terminal.
4. The GUI will open, presenting a button to select a folder.
5. Click "Select Folder" and choose the folder containing the MP4 files you wish to analyse.
6. The script will scan the folder for MP4 files, compute their durations, and display the results in a table within the GUI.

### Why was this created?

- To allow users to quickly and efficiently obtain the duration of multiple MP4 files within a specific directory.
- To provide a user-friendly interface for non-technical users, streamlining the process of video file analysis.

---

## Non-Developer Description 🙍‍♂️

### Project Overview:

This tool is designed to help users find out the duration of MP4 video files within a specific folder on their computer. By simply selecting a folder, the tool scans through all the MP4 files, calculates their durations, and displays the results in an easy-to-read table.

### How it Works:

- Upon launching, a window appears with a button labelled "Select Folder".
- Clicking the button allows you to choose the folder containing the MP4 files you wish to examine.
- Once a folder is selected, the tool scans through all the MP4 files in the folder, calculates their durations, and displays the results in a table within the same window.

### Why was this created?

- To offer a simple and intuitive way for users to find out the durations of multiple MP4 files without any technical expertise.
- To save time and provide a hassle-free experience in managing and organising video files.
