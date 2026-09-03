# Image Batch Processor

## 1. Project Overview

Image Batch Processor is a Python-based application designed to process multiple images from a selected directory. The application provides common image-processing operations such as resizing, rotation, cropping, and format conversion.

The project was developed to demonstrate practical implementation of Python programming concepts including Object-Oriented Programming, exception handling, file and directory management, custom exceptions, and image processing using the Pillow library.

---

## 2. Features

The application provides the following features:

* Read supported image files from a directory
* Display basic image information
* Select all images or specific images
* Resize images
* Rotate images
* Crop images
* Convert images to another format
* Process multiple images in a batch
* Save processed images to an output directory
* Handle invalid user input
* Handle image-processing errors
* Generate a processing summary

---

## 3. Technologies Used

* Python 3
* Pillow (PIL)
* OS module
* Object-Oriented Programming
* Exception Handling
* Custom Exceptions

---

## 4. Supported Image Formats

The application currently supports the following formats:

```text
.jpg
.jpeg
.png
.bmp
.webp
```

The application also supports uppercase and mixed-case file extensions.

Examples:

```text
image.jpg
image.JPG
image.PNG
image.WebP
```

---

## 5. Project Structure

```text
IMAGE_PROCESSING_PROJECT/
│
├── main.py
├── MainApp.py
├── IMAGE_READER_FILE.py
├── IMAGE_INFORMATION.py
├── ImageProcessor.py
├── BatchProcessor.py
├── Exception_handling.py
│
├── imagesdata/
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
│
└── output/
    ├── resize_image1.jpg
    ├── rotate_image2.png
    └── ...
```

---

## 6. Application Architecture

```text
main.py
   |
   v
MainApp
   |
   +------------------+
   |                  |
   v                  v
ImageReader       ImageInfo
   |
   v
BatchProcessor
   |
   v
ImageProcessor
   |
   v
Pillow
```

### Module Responsibilities

| Module/Class       | Responsibility                                             |
| ------------------ | ---------------------------------------------------------- |
| MainApp            | Controls application flow and handles user interaction     |
| ImageReader        | Reads supported image files from the selected directory    |
| ImageInfo          | Displays information about an image                        |
| ImageProcessor     | Performs image-processing operations                       |
| BatchProcessor     | Processes multiple images and generates processing results |
| Exception_handling | Contains application-specific custom exceptions            |

---

## 7. Installation

### Prerequisites

Python 3 must be installed on the system.

### Install Pillow

Open a terminal in the project directory and execute:

```bash
pip install Pillow
```

To verify the installation:

```bash
python -c "from PIL import Image; print('Pillow installed successfully')"
```

---

## 8. Running the Application

Execute the following command from the project directory:

```bash
python main.py
```

The application will ask the user to provide the directory containing the images.

Example:

```text
IMAGE BATCH PROCESSOR

PLEASE SELECT THE FOLDER CONTAINING YOUR IMAGES

Select folder
imagesdata
```

---

## 9. Application Workflow

### Step 1: Select Image Directory

The user provides the path of the directory containing the images.

The application scans the directory and identifies files with supported image extensions.

### Step 2: Select Images

The application displays the available images and allows the user to choose either:

```text
s - Select specific files
a - Select all files
```

### Step 3: Select an Operation

The available operations are:

```text
resize
rotate
crop
imageconverter
```

### Step 4: Provide Required Input

Depending on the selected operation, the application requests the required values from the user.

### Step 5: Batch Processing

The selected images are processed one by one.

If an image fails during processing, the error is handled and the application continues processing the remaining images.

### Step 6: Generate Summary

After processing is completed, the application displays the number of successfully processed and failed files.

---

## 10. Image Operations

### Resize

The user provides the required image dimensions.

Example:

```text
PLEASE ENTER A NEW LENGTH: 500
PLEASE ENTER A NEW WIDTH: 500
```

The resized images are saved in the output directory.

### Rotate

The user provides a rotation angle.

Example:

```text
PLEASE ENTER THE ANGLE VALUE: 90
```

The rotated images are saved in the output directory.

### Crop

The user provides four crop coordinates:

```text
Left
Top
Right
Bottom
```

Example:

```text
ENTER YOUR LEFT COORDINATES: 0
ENTER THE TOP COORDINATES: 0
ENTER THE RIGHT COORDINATES: 500
ENTER THE BOTTOM COORDINATES: 500
```

The coordinates are passed to Pillow in the following form:

```text
(left, top, right, bottom)
```

### Image Conversion

The user specifies the desired output format.

Example:

```text
Enter the format in which you want to convert your image: png
```

The converted image is saved with `_converted` added to its filename.

Example:

```text
image1.jpg
```

becomes:

```text
image1_converted.png
```

---

## 11. Exception Handling

The application implements exception handling to prevent invalid input and processing errors from terminating the program.

Custom exceptions are used for application-specific validation, including:

* Invalid file selection
* Invalid file count
* Invalid file position
* Invalid image dimensions
* Invalid crop coordinates
* Invalid image format

The application also handles built-in Python exceptions such as `ValueError`.

For invalid user input, the application uses loops to allow the user to enter the value again.

---

## 12. Output

Processed images are stored in the `output` directory.

If the directory does not exist, the application creates it automatically.

Example:

```text
output/
│
├── resize_image1.jpg
├── resize_image2.png
├── rotate_image3.jpg
├── crop_image4.webp
└── image5_converted.png
```

---

## 13. Processing Summary

After processing the selected images, the application displays a summary.

Example:

```text
Files successfully added in the output directory: 14
files failed during the processing: 0
```

If an individual image cannot be processed, it is counted as a failed file while the application continues processing the remaining files.

---

## 14. Testing

The application has been tested for the following scenarios:

1. Valid folder
2. Invalid folder
3. Empty folder
4. Supported image formats
5. Uppercase image extensions
6. Selecting all files
7. Selecting specific files
8. Invalid file selection
9. Invalid file count
10. Invalid file position
11. Valid resize
12. Invalid resize dimensions
13. Invalid resize input
14. Valid rotation
15. Invalid rotation input
16. Valid crop
17. Negative crop coordinates
18. Invalid crop coordinate relationships
19. Valid image conversion
20. Batch processing and error handling

---

## 15. Python Concepts Demonstrated

This project demonstrates the practical use of:

* Classes and objects
* Static methods
* Functions
* Conditional statements
* Loops
* Exception handling
* Custom exceptions
* `try` and `except`
* `raise`
* File and directory handling
* `os.listdir()`
* `os.path.join()`
* `os.path.basename()`
* `os.path.splitext()`
* Pillow image processing
* Batch processing
* Modular programming

---

## 16. Future Improvements

Possible future improvements include:

* Graphical User Interface
* Folder selection through a file dialog
* Progress indicator
* Additional image formats
* Image filters
* Brightness and contrast adjustment
* Image compression
* Watermarking
* Configurable output directory
* Detailed logging
* Additional image-processing operations

---

## 17. Conclusion

The Image Batch Processor provides a simple command-line interface for performing common image-processing operations on multiple files.

The project demonstrates how Python can be used to combine Object-Oriented Programming, file management, exception handling, custom exceptions, and the Pillow library into a practical application.
