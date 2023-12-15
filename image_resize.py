from PIL import Image

def resize_image_with_aspect_ratio(input_path, output_path, max_size):
    with Image.open(input_path) as img:
        img.thumbnail(max_size)
        
        img.save(output_path)

# Example usage
input_image_path = 'images/1.jpg'
output_image_path = 'images/resized_image.jpg'
max_size = (500, 500)

resize_image_with_aspect_ratio(input_image_path, output_image_path, max_size)
