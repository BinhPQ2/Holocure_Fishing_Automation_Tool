from PIL import Image, ImageDraw

# Get user input for top, left, width, and length
top = float(input("Enter top: "))
left = float(input("Enter left: "))
width = float(input("Enter width: "))
length = float(input("Enter length: "))

image_dir = "assets/sample.png"
# Load an example image (replace with your image path)
image = Image.open(image_dir)

# Create a copy of the image to draw on
image_with_square = image.copy()

# Draw a red square on the image
draw = ImageDraw.Draw(image_with_square)
draw.rectangle([left, top, left + width, top + length], outline='red', width=5)

# Show the image with the red square
image_with_square.show()
