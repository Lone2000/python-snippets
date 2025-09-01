"""
NOAA Climate Data Scraper
-------------------------

This script scrapes the NOAA Local Climatological Data (LCD) directory for a given year,
finds a file that matches a target file size, and downloads it.

Why use this?
-------------
- Automates searching and downloading datasets from NOAA's open data portal.
- Uses asynchronous HTTP requests for efficient fetching.
- Parses the HTML table to identify files and their metadata.
- Saves the matched CSV file into a local `download/` folder.

Libraries Used:
---------------
- asyncio / aiohttp : For asynchronous requests (faster than requests when scaled).
- BeautifulSoup4   : To parse the HTML table containing file info.
- pandas           : (Imported but not used here — can be useful if you process the CSV later).
- os               : For file and directory management.
"""

import pandas
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


async def fetch_html(url: str) -> bytes:
    """
    Fetch the raw HTML content of a webpage asynchronously.

    Args:
        url (str): The URL of the page to fetch.

    Returns:
        bytes: The raw HTML content of the page.
    """
    async with aiohttp.ClientSession() as session:  # Open async session
        async with session.get(url) as response:
            return await response.read()  # Get page content as bytes


async def main():
    """
    Main entry point of the scraper.

    - Requests the NOAA LCD directory page for 2021.
    - Parses the HTML to find files listed in the table.
    - Matches a file based on its 'size' column.
    - Downloads the matched CSV into a `download/` folder.
    """
    # Base directory for 2021 NOAA LCD data
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

    # Target file size (used to match a file in the table)
    size = '3774993'

    # Fetch and parse HTML
    html = await fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")  # Parse HTML with BeautifulSoup

    # Find the first table and extract its header row
    table = soup.find('table')
    header_row = table.find("tr")
    headers = [th.get_text(strip=True) for th in header_row.find_all('th')]  # Extract headers (th tags)

    # Get all rows except the first two (header + one extra row)
    data_rows = table.find_all('tr')[2:]

    # Iterate through rows to find a match based on file size
    for row in data_rows:
        cols = [td.get_text(strip=True) for td in row.find_all('td')]  # Extract each cell in row
        for data in cols:
            if size == data:
                print("MATCH FOUND:", cols)
                file_name = cols[0]  # File name is in the first column

                # Build the download URL for the matched file
                url = f"https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/{file_name}"

    # Print final file URL
    print(url)

    # Download the matched CSV file
    csv = await fetch_html(url)

    # Ensure 'download' directory exists
    if not os.path.isdir('download'):
        os.mkdir('download')  # Create folder if missing

    download_dir = 'download'
    full_path = os.path.join(download_dir, file_name)

    # Save the CSV file locally
    with open(full_path, 'wb') as f:
        f.write(csv)
        f.close()  # (Optional — already handled by 'with' context manager)


if __name__ == "__main__":
    asyncio.run(main())
