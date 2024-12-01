import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import csv
from collections import Counter

# Base directory where main.py is located
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR  # Set output directory to Z:/Foundry

# Load fonts from system
FONT_REGULAR = ImageFont.truetype("arial.ttf", 16)  # Regular Arial for files
FONT_BOLD = ImageFont.truetype("arialbd.ttf", 16)   # Arial Black for folders

def generate_file_type_csv(tree_content, output_file):
    """
    Generate a CSV file listing file types and their counts, sorted by count (descending).
    :param tree_content: List of tuples (content, type, extension).
    :param output_file: Path to save the CSV file.
    """
    # Count file types from the directory tree
    file_extensions = [ext for _, item_type, ext in tree_content if item_type == "file"]
    file_type_counts = Counter(file_extensions)

    # Sort file types by count in descending order
    sorted_file_types = sorted(file_type_counts.items(), key=lambda x: x[1], reverse=True)

    # Write to CSV
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["fileType", "count"])
        for file_type, count in sorted_file_types:
            writer.writerow([file_type if file_type else "no extension", count])

# Function to generate directory tree
def get_directory_tree(base_dir, recurse=True):
    """
    Generate a directory tree as a list of tuples (content, type, extension).
    :param base_dir: Base directory to start the tree.
    :param recurse: Whether to recursively include subdirectories.
    :return: A list of tuples where each tuple is (content, type, extension).
    """
    tree_items = []
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".")]  # Ignore hidden directories
        level = root.replace(base_dir, "").count(os.sep)
        indent = " " * 4 * level

        # Add folder
        tree_items.append((f"{indent}{Path(root).name}/", "folder", None))

        # Add files
        subindent = " " * 4 * (level + 1)
        for file in files:
            ext = Path(file).suffix[1:].lower()  # Get file extension without the dot, in lowercase
            tree_items.append((f"{subindent}{file}", "file", ext))
        if not recurse:
            break
    return tree_items

# Function to create an image from the directory tree with styling
def create_tree_image(tree_content, output_file):
    """
    Create an image representation of the directory tree with styling.
    :param tree_content: List of tuples (content, type, extension).
    :param output_file: Path to save the image.
    """
    # Define font sizes
    font_size = 16

    lines = [item[0] for item in tree_content]
    max_width = max(len(line) for line in lines) * font_size // 2
    max_height = len(lines) * font_size + 20

    # Create a blank image
    image = Image.new("RGB", (max_width, max_height), "white")
    draw = ImageDraw.Draw(image)

    # Colors for different file types
    # Text Files: Shades of blue.
    # Scripts/Code: Shades of green.
    # Images: Shades of purple.
    # Data Files: Orange and related shades.
    # Configuration/Meta Files: Shades of gray or yellow.
    colors = {
        "folder": "black",  # Folders remain black
        "rmd": "darkblue",  # R Markdown files
        "csv": "orange",  # CSV data files
        "pdf": "darkred",  # PDFs are dark red
        "png": "purple",  # Images
        "jpg": "purple",  # Images
        "gif": "purple",  # Images
        "r": "forestgreen",  # R scripts
        "py": "green",  # Python scripts
        "html": "red",  # HTML files
        "log": "brown",  # Log files
        "pyc": "darkgreen",  # Compiled Python files
        "txt": "blue",  # Plain text files
        "nb": "teal",  # Notebook files
        "json": "darkorange",  # JSON configuration or data
        "css": "lightblue",  # CSS files
        "md": "gray",  # Markdown files
        "ino": "olive",  # Arduino sketches
        "fbx": "gold",  # FBX 3D files
        "stl": "darkgoldenrod",  # STL 3D files
        "js": "lightgreen",  # JavaScript files
        "sh": "darkslategray",  # Shell scripts
        "3dm": "darkviolet",  # Rhino 3D files
        "yml": "yellow",  # YAML configuration
        "sql": "royalblue",  # SQL files
        "no extension": "black",  # No extension
        "default": "gray",  # Default fallback for unspecified types
    }

    # Draw the directory tree text
    y = 10
    for line, item_type, ext in tree_content:
        if item_type == "folder":
            font = FONT_BOLD
            color = colors["folder"]
        else:
            font = FONT_REGULAR
            color = colors.get(ext, colors["default"])  # Use extension to determine color
        draw.text((10, y), line, fill=color, font=font)
        y += font_size

    # Save the image
    image.save(output_file)

# Function to create README.md referencing the image
def create_readme_with_image(image_file):
    """
    Create a README.md file referencing the generated image.
    :param image_file: Path to the generated image.
    """
    readme_file = OUTPUT_DIR / "xREADME.md"
    relative_image_path = Path(image_file).relative_to(OUTPUT_DIR)

    with open(readme_file, "w", encoding="utf-8") as file:
        file.write(f"![Directory Tree]({relative_image_path})\n")

# Generate directory tree content for Z:/Foundry (excluding dirTrees itself)
target_directory = BASE_DIR  # Target is the parent of dirTrees
directory_tree = get_directory_tree(str(target_directory))

# Create the tree image
tree_image_file = OUTPUT_DIR / "directory_tree.png"
create_tree_image(directory_tree, tree_image_file)

# Create the README.md file
create_readme_with_image(tree_image_file)

# Generate fileTypes.csv
csv_file_path = BASE_DIR / "fileTypes.csv"
generate_file_type_csv(directory_tree, csv_file_path)