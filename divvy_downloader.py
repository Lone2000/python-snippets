"""
Divvy Data Downloader & Extractor
---------------------------------

This script downloads multiple ZIP files from a list of URLs, saves them into a
`downloads/` folder, extracts their contents, and removes the original ZIPs.

Usage:
    python divvy_downloader.py

Why use this?
-------------
- Automates bulk dataset downloads (e.g., bike-share, open data portals, Kaggle).
- Handles directory creation automatically.
- Cleans up by removing ZIP files after extraction.
- Prints status messages for quick debugging.

Modify:
-------
- Add or remove URLs in `download_uris` list.
- Change the `downloads_dir` path if needed.
"""

import requests
import os
import sys
import zipfile

# List of datasets to download (add your own URLs here)
download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    # Example of broken URL to test error handling
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def download_and_extract(url: str, downloads_dir: str = "downloads") -> None:
    """
    Download a ZIP file from the given URL, extract its contents, and remove it.

    Args:
        url (str): URL of the ZIP file to download.
        downloads_dir (str): Directory where files will be saved & extracted.
    """
    # Get the filename from the URL
    filename = url.split("/")[-1]
    file_path = os.path.join(downloads_dir, filename)

    print(f"Downloading: {filename}")

    # Make request to server
    response = requests.get(url)
    if response.status_code == 200:
        # Save ZIP file locally
        with open(file_path, "wb") as f:
            f.write(response.content)

        # Extract ZIP contents
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(downloads_dir)

        print(f"Extracted: {filename}")

        # Remove original ZIP
        os.remove(file_path)
        print(f"Removed ZIP: {filename}")

    else:
        print(f"Failed to download {filename} | Status: {response.status_code}")


def main():
    """
    Main function that loops over all URLs and downloads them.
    """
    downloads_dir = "downloads"

    # Ensure the downloads folder exists
    if not os.path.isdir(downloads_dir):
        os.mkdir(downloads_dir)
        print(f"Created directory: {downloads_dir}")

    # Process each file
    for url in download_uris:
        download_and_extract(url, downloads_dir)

    print("All downloads processed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
