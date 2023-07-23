# File Extension Converter

The File Extension Converter is a Python script designed to automate the process of changing file extensions for all files in the directory where it is present. The script provides a simple way to specify the old extension and the new extension for the files, and it will take care of renaming the files accordingly.

## How to Use

1. **Prerequisites**:
   - Python 3.x installed on your system.

2. **Run the Script**:
   - Place the `main.py` script in the directory containing the files you want to convert.

   - **Method 1: Command Line**
     - Open a terminal or command prompt in the directory containing the script.
     - Run the following command:
       ```
       python main.py
       ```

   - **Method 2: Double-click**
     - You can also run the script by double-clicking on the `main.py` file in the file explorer. This will automatically execute the script and convert the file extensions.

3. **Follow the Prompts**:
   - When prompted, enter the old extension of the files you want to convert (e.g., mp4).
   - Next, enter the new extension you wish to convert the files to (e.g., avi).

The script will then process all files in the current directory and change the extension of files that match the old extension you provided.

## Example

Suppose you have the following files in the same directory as the `main.py` script:
- `file1.mp4`
- `file2.mp4`
- `document.txt`

If you run the script and specify the old extension as "mp4" and the new extension as "avi," the script will rename `file1.mp4` and `file2.mp4` to `file1.avi` and `file2.avi`, respectively. The `document.txt` file will remain unaffected.

## Use Case Scenarios

The File Extension Converter can be helpful in various scenarios, including:

1. **Bulk Conversion of Files**: When you have a collection of files with a specific file extension, and you want to change them all to a different extension, this script can save you time and effort by automatically performing the conversions.

2. **Media File Conversion**: Suppose you have multiple media files like videos or audio files with one file format, and you need to convert them to another format to be compatible with a specific media player or application. This script can streamline the conversion process.

3. **Data File Management**: If you have datasets or data files with a particular extension that you want to change for consistency or compatibility reasons, the script can help you achieve that without having to rename each file manually.

4. **Cleaning Up File Extensions**: In some cases, you might have received files with incorrect or undesirable extensions. This script allows you to quickly standardize and clean up the file extensions in a directory.

## Caution

- **Backup**: It's always a good idea to create a backup of your files before running the script, especially if you're unsure about the consequences of changing certain file extensions.

- **Single Directory**: This script processes files only in the directory where it is located and does not handle subdirectories.

## Requirements

- Python 3.x
- Operating System: Windows, macOS, or Linux

---
