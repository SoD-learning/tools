# PDF Splitter

## Contents

- [Description for Developers](#developer-description)
- [Description for Non-Developers](#non-developer-description)

## Developer Description 👨‍💻

### Project Overview:

This utility is designed for easy and efficient splitting of PDF files into individual pages or extracting specific page ranges. Users select a PDF file through a simple GUI, specify their splitting preferences, and the script then processes the PDF, saving the output as separate PDF files or a subset based on the user's choice.

### Technology Used

- Python
- Tkinter for the GUI
- PyPDF2 for PDF processing

### File Structure:

- `split-pdf.py`: The main script that includes the GUI and splitting logic.

### Usage:

1. Ensure you have Python installed on your system.
2. Install the necessary Python packages: `pip install PyPDF2`
3. Run `split-pdf.py`. This will open a GUI prompting you to select a PDF for splitting.
4. Choose the split options (every page or specific page range) and proceed with 'Split PDF'. You will be prompted to select a save location for the resulting PDF files.

### Why was this created?

- To automate the process of splitting PDF files, providing a quick and error-free way to generate individual pages or specific subsets of a document.
- This tool is invaluable for tasks such as document management, digital archiving, and content segmentation, where selective pages of a document need to be isolated or shared.

---

## Non-Developer Description 🙍‍♂️

### Project Overview:

This tool helps you break down large PDF documents into smaller pieces, either by separating each page or by selecting specific portions. This is useful for extracting relevant content, sharing specific sections, or managing content on a more precise level.

### How it Works:

- The user launches the tool, which displays a straightforward window with instructions.
- Through this window, the user selects a PDF document stored on their computer.
- After choosing the PDF, the user specifies how they want to split the PDF and clicks on 'Split PDF'. The tool then asks where to save the new files.
- The tool processes the selected PDF and saves the split content as new PDF files in the chosen location.

### Why was this created?

- To provide an effortless way of dissecting PDF files into smaller, manageable parts or specific segments based on user requirements.
- It aids in document organisation, making it simpler to locate, share, and utilise content within bulky documents.
