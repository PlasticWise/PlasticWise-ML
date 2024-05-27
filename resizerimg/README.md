# Image Resizing Script

This script resizes images to 224x224 pixels for use in your project.

## Requirements

Make sure you have Python installed on your machine. You'll also need the `Pillow` library. You can install it using pip:

```bash
pip install pillow
```

## Usage

1. **Prepare your folders:**
   - Create a folder containing the images you want to resize. Let's call this `input_folder`.
   - Create another folder where the resized images will be saved. Let's call this `output_folder`.

2. **Update the script:**
   - Open the `resize_images.py` script.
   - Update the `input_folder` and `output_folder` variables with the paths to your input and output folders.

3. **Run the script:**
   - Navigate to the directory containing the `resize_images.py` script.
   - Run the script using Python:

```bash
python resize_images.py
```

## Script Explanation

Here is a breakdown of the script:

```python
from PIL import Image
import os

def resize_images(input_folder, output_folder, size=(224, 224)):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            # Open image
            img = Image.open(os.path.join(input_folder, filename))
            # Resize image
            img_resized = img.resize(size)
            # Save resized image to the output folder
            img_resized.save(os.path.join(output_folder, filename))

# Example usage
input_folder = 'path/to/input/folder'  # Replace with your input folder path
output_folder = 'path/to/output/folder'  # Replace with your output folder path

resize_images(input_folder, output_folder)
```

### Parameters
- `input_folder`: The path to the folder containing the original images.
- `output_folder`: The path to the folder where resized images will be saved.
- `size`: The target size for resizing. Default is (224, 224).

### What the Script Does
- Checks if the output folder exists; if not, it creates it.
- Iterates through each file in the input folder.
- Opens and resizes each image to 224x224 pixels.
- Saves the resized image to the output folder with the same filename.

## Notes
- Ensure the input folder contains only image files with extensions `.jpg`, `.png`, or `.jpeg`.
- The resized images will overwrite any existing files in the output folder with the same name.

## Example
Assuming your input images are in `./images/input` and you want to save resized images to `./images/output`, you would set:

```python
input_folder = './images/input'
output_folder = './images/output'
```

Then, run the script to resize your images.

## Contact
If you have any questions, feel free to reach out to the project maintainer.

Happy resizing!

