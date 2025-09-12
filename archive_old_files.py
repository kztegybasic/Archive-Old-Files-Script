import os
import zipfile
import time
from datetime import datetime, timedelta

def archive_old_files(folder_path, archive_name="archived_files.zip", days_old=30):
    """
    Archives (zips) all files in the specified folder that were modified more than `days_old` days ago.

    Args:
        folder_path (str): The path to the folder to search files in.
        archive_name (str): The name of the zip archive to create.
        days_old (int): The minimum age of files to archive (in days).
    """
    cutoff = time.time() - days_old * 86400  # 86400 seconds in a day
    files_to_archive = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_full_path = os.path.join(root, file)
            if os.path.isfile(file_full_path):
                modified_time = os.path.getmtime(file_full_path)
                if modified_time < cutoff:
                    files_to_archive.append(file_full_path)

    if not files_to_archive:
        print(f"No files older than {days_old} days found in {folder_path}.")
        return

    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in files_to_archive:
            arcname = os.path.relpath(file_path, folder_path)
            zipf.write(file_path, arcname)
            print(f"Archived: {file_path}")

    print(f"\nArchived {len(files_to_archive)} files to {archive_name}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Archive files older than N days.")
    parser.add_argument("folder", help="Folder to scan for old files")
    parser.add_argument("--archive", default="archived_files.zip", help="Name of the output zip file")
    parser.add_argument("--days", type=int, default=30, help="Minimum age (in days) of files to archive")

    args = parser.parse_args()
    archive_old_files(args.folder, args.archive, args.days)
