from PIL import Image

# ASCII character set used to create the ASCII art
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Resize the image to a smaller size
def resize_image(image, new_width=100):
    width, height = image.size
    new_height = new_width * height // width
    return image.resize((new_width, new_height))

# Convert each pixel to an ASCII character based on its intensity
def pixel_to_ascii(pixel):
    gray = sum(pixel) // 3
    index = gray * (len(ASCII_CHARS) - 1) // 255
    return ASCII_CHARS[index]

# Convert the image to ASCII art
def image_to_ascii(image, width):
    pixels = image.getdata()
    ascii_chars = [pixel_to_ascii(pixel) for pixel in pixels]
    ascii_art = ''.join(ascii_chars)
    
    # Add line breaks after the specified width
    ascii_art_lines = [ascii_art[i:i+width] for i in range(0, len(ascii_art), width)]
    return '\n'.join(ascii_art_lines)

# Load the image
useThisImage = input('Please input your image name with ext: ')
image = Image.open(useThisImage)

# Resize the image to a smaller size
image = resize_image(image)

# Convert the image to ASCII art
ascii_art = image_to_ascii(image, 100)

# Save the ASCII art to a text file
with open('ascii_art.txt', 'w') as f:
    f.write(ascii_art)
    
# Print a message indicating the file has been saved
print('ASCII art saved to ascii_art.txt')
