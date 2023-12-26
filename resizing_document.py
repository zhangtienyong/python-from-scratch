from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def resize_image(input_path, output_path, max_file_size_kb=2048, max_page_count=3):
    # Open the image file
    with Image.open(input_path) as img:
        # Resize the image
        img = img.resize((800, 800))  # Adjust the dimensions as needed

        # Save the resized image to the output path
        img.save(output_path)

def create_pdf(input_image_path, output_pdf_path):
    # Create a new PDF document
    pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=letter)

    # Add the resized image to the PDF
    pdf_canvas.drawImage(input_image_path, 100, 100)  # Adjust the position as needed

    # Save the PDF
    pdf_canvas.save()

def process_scanned_document(input_path, output_path):
    # Resize the document
    resized_image_path = "images/resized_document.jpg"
    resize_image(input_path, resized_image_path)

    # Check if the file size is within the limit
    if os.path.getsize(resized_image_path) > 2 * 1024 * 1024:
        print("Error: File size exceeds the limit of 2 MB.")
        return

    # Check if the document has more than 3 pages
    with Image.open(resized_image_path) as img:
        page_count = getattr(img, "n_frames", 1)  # Get the number of frames/pages
        if page_count > 3:
            print("Error: Document contains more than 3 pages.")
            return

    # Create a PDF with the resized image
    create_pdf(resized_image_path, output_path)
    print("Document resized and saved as PDF successfully.")

# Example usage:
input_file_path = "images/input_document.jpg"  # Replace with the actual input file path
output_file_path = "images/resized_document.pdf"  # Replace with the desired output file path

process_scanned_document(input_file_path, output_file_path)
