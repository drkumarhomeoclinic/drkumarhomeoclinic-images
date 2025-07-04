from PIL import Image
import os

def resize_images(input_dir, output_dir, size):
    """
    Resizes all images in a directory to a specified size and saves them to another directory.

    Args:
        input_dir: The path to the directory containing the images to be resized.
        output_dir: The path to the directory where the resized images will be saved.
        size: A tuple (width, height) specifying the new size for the images.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                img_path = os.path.join(input_dir, filename)
                img = Image.open(img_path)
                img_resized = img.resize(size)
                output_path = os.path.join(output_dir, filename)
                img_resized.save(output_path)
                print(f"Resized {filename} and saved to {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    input_directory = "Clinic"  # Replace with the actual path to your images
    output_directory = "clinic-light" # Replace with the desired output path
    target_size = (800, 600) # Replace with the desired width and height

    resize_images(input_directory, output_directory, target_size)