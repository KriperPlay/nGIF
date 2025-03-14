# nGIF
![logo](https://github.com/user-attachments/assets/d15cc269-002c-4bbe-8767-aa74dc628827)

# Overview

// Documentation written by gpt-4o

The nGIF project is a graphical user interface (GUI) application developed using PyQt6 that allows users to create GIFs from a collection of images. Users can add images, preview them, delete images, and save the final GIF with a specified duration between frames.

# Features

• Image Loading: Users can load images in PNG, JPG, or JPEG format.

• Image Preview: The application displays the currently selected image in the GUI.

• Image Management: Users can add multiple images to the project and remove them as needed.

• GIF Creation: Users can create a GIF from the selected images and specify the duration for all frames.

• File Saving: The application allows users to save the created GIF to a specified location.

• GitHub Link: A menu option provides a link to the project's GitHub repository for further exploration or contribution.

# Requirements

• Python 3.x

• PyQt6

• NumPy

• imageio

# Installation

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/KriperPlay/nGIF/
   cd nGIF
    ```
2. Run unix.sh or windows.bat
   ```
   # if unix
   chmod +x build-scripts/unix.sh
   ./build-scripts/unix.sh

   #if windows
   ./build-scripts/windows.sh

# Usage

1. Run the Application:
   After build, binary file will be in root dir

3. Add Images:

   • Click on the "Add Image" button to open a file dialog.

   • Select an image file (PNG, JPG, or JPEG).

   • The selected image will be displayed in the preview area, and its path will be added to the list.

   • All images must be the same resolution

5. View Images:

   • Select an image from the dropdown list to view it in the preview area.

6. Delete Images:

   • Select an image from the dropdown list and click on the "Delete Image" button to remove it from the list and reset the preview.

7. Create GIF:

   • Specify a duration(in milliseconds) for all frames using the spin box.

   • Click on "Save" to open a file dialog and choose where to save the generated GIF.

8. Start a New File:

   • Click on "New File" to clear all current images and start a new project.

9. Access GitHub Repository:

   • Click on the "GitHub" menu option to open the project's GitHub page in your web browser.

# Screenshots
![изображение](https://github.com/user-attachments/assets/30b58880-877e-4822-8a4b-dbc4ff8f9b3c)


