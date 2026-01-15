def load_image(path):
    print(f"Reading image from {path}")
    return path

def to_gray(img):
    if img is None:
        raise ValueError("No image provided")
    print("Converting image to grayscale")
    grayscale_image = "grayscale_image"
    return grayscale_image

def display(img):
    print(f"Displaying {img}")