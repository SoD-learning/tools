# Image to PDF Converter

## Contents

- [Description for Developers](#developer-description)
- [Description for Non-Developers](#non-developer-description)

## Developer Description 👨‍💻

### Project Overview:

This utility is designed for the simple and efficient conversion of images into a single PDF file. It allows users to select multiple images from their file system, which the script then converts into a PDF, saving it at a user-defined location.

### Technology Used

- Python
- Tkinter for the GUI
- Pillow for image processing
- FPDF for PDF creation

### File Structure:

- `img-to-pdf.py`: The main script that includes the GUI and conversion logic.

### Usage:

1. Ensure you have Python installed on your system.
2. Install the necessary Python packages: `pip install Pillow fpdf`
3. Run `img-to-pdf.py`. This will open a GUI prompting you to select images for conversion.
4. Select the images and choose the 'Convert to PDF' option. You will be prompted to select a save location for the resulting PDF.

### Why was this created?

- To automate the process of converting images to PDF, providing a quick and error-free way to generate PDF documents from a series of images.
- This tool simplifies tasks such as document scanning, ebook creation, and the consolidation of images into a single, easily shared format.

---

## Non-Developer Description 🙍‍♂️

### Project Overview:

This tool helps you convert scanned documents, illustrations, or photos into a single PDF file. This is useful for digital archiving, creating ebooks, or sharing a collection of images in a universal format.

### How it Works:

- The user opens the tool, which provides a simple window with instructions.
- Through this window, the user can select multiple images from their computer.
- After selecting the images, the user clicks on 'Convert to PDF', and the tool asks where to save the PDF.
- The tool quickly processes the images and saves them as a single PDF file in the chosen location.

### Why was this created?

- To provide a hassle-free way of combining images into a single, easily shared PDF file.
- It assists in organizing digital files and helps in the creation of documents that can be uniformly opened and viewed on any device.
