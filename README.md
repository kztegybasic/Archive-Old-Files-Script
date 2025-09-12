# Archive Old Files Script

This Python script archives (zips) all files in a specified folder that were modified more than a given number of days ago (default is 30 days).

## Features

- Recursively scans a folder and its subfolders
- Archives only files older than a set number of days (default: 30)
- Outputs a ZIP file containing the archived files

## Usage

1. **Save the script** as `archive_old_files.py`.

2. **Run the script** from the command line:

   ```sh
   python archive_old_files.py /path/to/folder --archive old_files.zip --days 30
   ```

   - `/path/to/folder`: The folder to search for old files.
   - `--archive`: (Optional) Name of the output zip file. Defaults to `archived_files.zip`.
   - `--days`: (Optional) Minimum age (in days) of files to archive. Defaults to `30`.

## Example

Archive all files in `~/Documents/` older than 60 days into `backup.zip`:

```sh
python archive_old_files.py ~/Documents --archive backup.zip --days 60
```

## Requirements

- Python 3.x (no external packages needed)

## How It Works

- The script checks the last modified time of each file.
- If a file was last modified more than the specified number of days ago, it is added to the archive.
- The archive is saved with the given name in the current directory.

## License

This project is open source and available under the MIT License.
