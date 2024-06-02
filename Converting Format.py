import cv2
import os

# Input and output directories
input_dir = 'C:/Users/javie/Downloads/Styrofoam'  # Replace with your input folder path
output_dir = 'C:/Users/javie/Documents/Kuliah/Semester 6/Bangkit/Capstone/Dataset/Styrofoam Rev'  # Replace with your output folder path

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# List all files in the input directory
files = os.listdir(input_dir)

# Filter image files (assuming common image formats)
image_extensions = ['.jpg', '.jpeg', '.bmp', '.tiff', '.png']

for file_name in files:
    # Get file extension
    ext = os.path.splitext(file_name)[1].lower()

    # Check if the file is an image
    if ext in image_extensions:
        # Full path to the input image
        input_path = os.path.join(input_dir, file_name)

        # Read the image
        image = cv2.imread(input_path)

        # Check if the image was successfully loaded
        if image is not None:
            # Construct the output file path
            output_file_name = os.path.splitext(file_name)[0] + '.png'
            output_path = os.path.join(output_dir, output_file_name)

            # Write the image as PNG
            cv2.imwrite(output_path, image)
            print(f"Image saved as {output_path}")
        else:
            print(f"Error: Could not load image {input_path}")
