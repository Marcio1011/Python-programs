import zipfile  # Provides tools to create and read ZIP files
import pathlib  # Helps work with file paths in a clean, cross-platform way


def make_archive(filepaths, dest_dir):
    """
    Creates a ZIP archive called 'compressed.zip' inside the destination folder.

    Parameters:
        filepaths (list): A list of file paths to include in the ZIP file.
        dest_dir (str): The folder where the ZIP file will be created.
    """

    # Build the full path to the output ZIP file (destination folder + filename)
    dest_path = pathlib.Path(dest_dir, "compressed.zip")

    # Create a new ZIP file in write mode ('w').
    # If the file already exists, it will be overwritten.
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # Loop through all file paths that should be added to the ZIP
        for filepath in filepaths:
            # Convert each path to a proper Path object for safety and compatibility
            filepath = pathlib.Path(filepath)

            # Add the file to the archive.
            # arcname ensures only the filename (not full path) is stored in the ZIP.
            archive.write(filepath, arcname=filepath.name)


