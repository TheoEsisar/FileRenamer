# Image Renamer

## Description

This Python script renames image files in a specified directory based on their last modified timestamps. It supports custom timestamp formats, dry run mode and MIME type filtering.

## Requirements

- Python 3.x
- tqdm library

Install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line and provide the necessary arguments:

```bash
python rename_images.py <directory_path> [--dry-run] [--format <format_choice>] [--mime-type-prefix <prefix>]
```

- `<directory_path>`: Path to the directory containing images to rename.
- `--dry-run`: Perform a dry run without renaming files (optional).
- `--format <format_choice>`: Choose a timestamp format (0-3). Default is 0 (%Y%m%d_%H%M%S).
- `--mime-type-prefix <prefix>`: Filter files by MIME type prefix (default: image).

## Examples

Rename images in a directory with default settings:

```bash
python rename_images.py /path/to/images
```

Perform a dry run with a custom timestamp format:

```bash
python rename_images.py /path/to/images --dry-run --format 1
```
