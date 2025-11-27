import FreeSimpleGUI as sg           # GUI library used to build desktop interfaces
from zip_creator import make_archive # Custom function that creates a ZIP archive


# -----------------------------
# UI ELEMENTS (Labels + Inputs)
# -----------------------------

# Text label telling the user to select files to compress
label1 = sg.Text("Select files to compress:")

# Input field that will display the selected file paths
input1 = sg.Input()

# File picker button that allows selecting multiple files
choose_button1 = sg.FilesBrowse("Choose", key="files")


# Text label telling the user to select the destination folder
label2 = sg.Text("Select destination folder:")

# Input field that will show the chosen folder
input2 = sg.Input()

# Folder picker button for choosing the output location
choose_button2 = sg.FolderBrowse("Choose", key="folder")


# Main button that triggers the compression process
compress_button = sg.Button("Compress")

# Text area used to display status messages (e.g., success notification)
output_label = sg.Text(key="output")


# -----------------------------
# WINDOW LAYOUT & CREATION
# -----------------------------

# Create the main application window.
# The 'layout' defines how all UI components are arranged on the screen.
window = sg.Window(
    "File Compressor",
    layout=[
        [label1, input1, choose_button1],
        [label2, input2, choose_button2],
        [compress_button, output_label]
    ]
)


# -----------------------------
# EVENT LOOP (Keeps App Running)
# -----------------------------

# The GUI stays alive inside this loop until the user closes the window.
while True:
    event, values = window.read()  # Read user interactions (button clicks, inputs)
    print(event, values)           # Debug print (optional)

    # Retrieve multiple selected file paths.
    # FilesBrowse returns paths separated by semicolons.
    filepaths = values["files"].split(";")

    # Retrieve selected destination folder
    folder = values["folder"]

    # Call the custom ZIP maker function
    make_archive(filepaths, folder)

    # Update the status label to confirm success
    window["output"].update(value="Compression completed")


window.close()