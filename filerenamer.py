import os
from datetime import datetime
from pathlib import Path
import mimetypes
import argparse
from tqdm import tqdm

def find_files(directory, mime_type_prefix='image'):
    files = []
    try:
        walk = os.walk(directory)
        for root, dirs, dir_files in walk:
            for file in dir_files:
                mime_type, _ = mimetypes.guess_type(file)
                # Check if the file matches the specified MIME type prefix
                if mime_type and mime_type.startswith(mime_type_prefix):
                    files.append(os.path.join(root, file))
    except Exception as e:
        print(f"Failed to find files in directory {directory}: {e}")
    return files

def rename_files_based_on_timestamp(directory_path, dry_run=False, timestamp_format='%Y%m%d_%H%M%S', mime_type_prefix='image'):
    try:
        directory_path = Path(directory_path).resolve()
        if not directory_path.exists():
            print(f"Directory {directory_path} does not exist.")
            return
        
        files = find_files(directory_path, mime_type_prefix=mime_type_prefix)
        
        for filename in tqdm(files, desc="Processing", unit="file"):
            full_file_path = Path(filename)
            modified_time = os.path.getmtime(full_file_path)
            formatted_timestamp = datetime.fromtimestamp(modified_time).strftime(timestamp_format)
            _, ext = os.path.splitext(filename)
            new_filename = f"{formatted_timestamp}{ext}"
            
            if dry_run:
                print(f"Dry run: Would rename '{filename}' to '{new_filename}'")
            else:
                os.rename(full_file_path, directory_path / new_filename)
    except Exception as e:
        print(f"An error occurred while renaming files: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files based on their last modified timestamp.")
    parser.add_argument("directory", type=str, help="Path of the directory whose files need to be renamed.")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without renaming files.")
    parser.add_argument("--format", type=int, choices=[0, 1, 2, 3], default=0,
                        help="Custom timestamp format (0: %Y%m%d_%H%M%S, 1: %Y %m %d %H%M%S, 2: %d%m%Y_%H%M%S, 3: %m%d%Y_%H%M%S). Default is 0.")
    parser.add_argument("--mime-type-prefix", type=str, default='image',
                        help="Filter files by MIME type prefix (default: image).")
    
    args = parser.parse_args()
    
    # Define timestamp formats based on user choice
    timestamp_formats = ['%Y%m%d_%H%M%S', '%Y %m %d %H%M%S', '%d%m%Y_%H%M%S', '%m%d%Y_%H%M%S']
    timestamp_format = timestamp_formats[args.format]
    
    rename_files_based_on_timestamp(args.directory, dry_run=args.dry_run, timestamp_format=timestamp_format,
                                    mime_type_prefix=args.mime_type_prefix)
