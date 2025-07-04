from PIL import Image
import os

def resize_images(input_dir, output_dir, max_size):
    """
    Resizes all images in a directory to fit within a specified max size while maintaining aspect ratio,
    and saves them to another directory.

    Args:
        input_dir: The path to the directory containing the images to be resized.
        output_dir: The path to the directory where the resized images will be saved.
        max_size: A tuple (max_width, max_height) specifying the maximum dimensions.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                img_path = os.path.join(input_dir, filename)
                img = Image.open(img_path)

                # Resize while maintaining aspect ratio
                img.thumbnail(max_size, Image.Resampling.LANCZOS)

                output_path = os.path.join(output_dir, filename)
                img.save(output_path, optimize=True, quality=85)
                print(f"Resized {filename} and saved to {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = "doctor"
    output_directory = "doctor-light"
    max_dimensions = (1200, 1200)

    resize_images(input_directory, output_directory, max_dimensions)
