# Obsidian Graph-Free Link Generator

A command-line utility to efficiently create graph-free, clickable Markdown links for your Obsidian vault. This tool is designed for Obsidian users who want to add navigational links within their notes without cluttering the graph view with connections that aren't conceptual.

It's perfect for MOCs (Maps of Content), dashboards, or daily notes where you need functional links to other notes, headings, or blocks, but don't want to create a visual dependency in the graph.

## Key Features

*   **Two Generation Modes**:
    *   **Manual Mode**: Quickly generate a single link by typing in a note title and display text.
    *   **Batch Mode**: Process an entire file of raw Obsidian URLs (`obsidian://...`) and assign display text to each one interactively.
*   **Clean Graph View**: All links generated are in the Obsidian URL format (`[text](obsidian://...)`), which makes them clickable in your vault but invisible to the graph view and backlinks pane.
*   **Organized File Structure**: Automatically uses dedicated folders (`Batch Processing` for input files, `Generated Links` for output) to keep your project directory clean.
*   **Overwrite Protection**: When saving, the script checks if a file with the same name already exists and asks for confirmation before overwriting, preventing accidental data loss.
*   **User-Friendly Output**: If you choose not to save your generated links to a file, the script prints them directly to the console for easy copying and pasting.

## Prerequisites

*   [Python 3.6](https://www.python.org/downloads/) or higher.

## Setup & Installation

1.  Clone this repository or download the `obsidian_link_generator.py` script to a folder on your computer.
2.  In the same folder as the script, create a new folder named `Batch Processing`.

Your folder structure should look like this:
`/your-project-folder
|-- obsidian_link_generator.py
|-- /Batch Processing/`

The script will automatically create a `Generated Links` folder for you the first time you save a file.

## How to Use

First, open a command prompt or terminal and navigate to the folder where you saved the script.
Then, run the script: python obsidian_link_generator.py


You will be prompted to choose a mode.

### Mode 1: Manual Input

1.  Select `1` for Manual Mode.
2.  Enter the exact title of the note you want to link to.
3.  Enter the display text for the link (or press Enter to use the note title as the text).
4.  The script will generate and display the link. You can create more links or proceed to save the output.

### Mode 2: Batch File

This mode is ideal for processing multiple links at once.

1.  **Prepare your input file**:
    *   In Obsidian, navigate to each note, heading, or block you want to link to.
    *   Use the command palette (`Ctrl/Cmd + P`) and run the command **"Copy Obsidian URL"**.
    *   Create a new `.txt` file inside your `Batch Processing` folder (e.g., `my_links.txt`).
    *   Paste each copied Obsidian URL into this file, one per line.
2.  **Run the script**:
    *   Select `2` for Batch File mode.
    *   Enter the name of your input file (e.g., `my_links.txt`).
    *   The script will show you each URL one by one and prompt you to enter the desired display text for it.
3.  **Save or View the Output**:
    *   After processing is complete, you can save all the generated links to a new file in the `Generated Links` folder or have them printed to the console.

> **Note**: The batch processing feature **only supports `.txt` files currently.**

## Future Development

This tool is fully functional, but future enhancements could include:

*   **GUI Version**: A simple graphical user interface using a library like Tkinter or PyQT.
*   **Clipboard Integration**: Automatically copy a generated link to the clipboard.
*   **Broader File Support**: Add support for processing `.csv` or `.md` files in batch mode.
