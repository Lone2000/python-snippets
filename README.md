# Python Snippet Library

A personal collection of **reusable Python scripts** for data engineering, web scraping, automation, and analysis.  
Instead of memorizing code, I keep well-documented snippets here — ready to copy, adapt, and reuse.

---

## 📌 Why this repo?
- **Efficiency**: Don’t waste time rewriting the same code.  
- **Reference**: Acts as a personal knowledge base.  
- **Reusability**: Scripts are modular and easy to drop into any project.  
- **Portfolio**: A living proof of coding practices and problem-solving style.  

---

## 📝 Snippets Overview

### Divvy Data Downloader
**Path:** `data_downloader/divvy_downloader.py`  

This script downloads multiple ZIP files from a list of URLs, saves them into a `downloads/` folder, extracts their contents, and removes the original ZIPs.  

**Features**  
- Automates bulk dataset downloads.  
- Handles directory creation automatically.  
- Cleans up by removing ZIP files after extraction.  
- Prints status messages for quick debugging.  

**Usage**  
```bash
python divvy_downloader.py
```

---

### NOAA Climate Data Scraper
**Path:** `web_scraping/noaa_scraper.py`  

This script uses **asyncio**, **aiohttp**, and **BeautifulSoup4** to scrape the NOAA Local Climatological Data (LCD) directory, match files by size, and download the matching CSV file.  

**Features**  
- Asynchronous HTML fetching.  
- Scrapes NOAA’s directory table.  
- Matches file based on `size` column.  
- Downloads the file into a `download/` folder.  

**Usage**  
```bash
pip install aiohttp beautifulsoup4 pandas
python noaa_scraper.py
```



