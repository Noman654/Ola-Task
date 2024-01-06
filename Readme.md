
# Web Scraping Script for ePaper Images

## Overview
This Python script is designed to automate the process of downloading images from the ePaper website "https://epapervijayavani.in/". It uses Selenium for web scraping to navigate through the website and download images of the newspaper pages.

## Features
- Automated navigation to the specified URL using Selenium WebDriver.
- Extracts all available ePaper images from the page.
- Saves the images in separate folders named after the paper edition.
- Utilizes both Selenium and Requests libraries for efficient scraping and downloading.

## Prerequisites
To run this script, you need to have the following installed:
- Python 3
- Selenium WebDriver
- ChromeDriver (or any other compatible driver for your browser)
- `requests` library

## Installation
1. **Python 3**: Make sure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Selenium WebDriver**: Install Selenium using pip:
   ```
   pip install selenium
   ```

3. **ChromeDriver**: Download ChromeDriver from its [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads). Ensure that the version of ChromeDriver matches the version of Chrome you are using. Add the ChromeDriver executable to your system's PATH.

4. **Requests Library**: Install the `requests` library using pip:
   ```
   pip install requests
   ```

## Usage
1. Set the `headless` option in the script to `True` or `False` depending on whether you want to see the browser window during the script execution.

2. Run the script using Python:
   ```
   python your_script_name.py
   ```
3. The script will navigate to the specified URL and begin downloading images, saving them in appropriately named folders according to the ePaper edition.

## Note
- The script is currently set up for "https://epapervijayavani.in/". If you wish to scrape a different website, you will need to modify the `url` and the elements' selectors as per the new website's HTML structure.


