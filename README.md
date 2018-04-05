# Marks-Scraper
This python script scrapes the marks of all CSE students of VTU 5th sem cbcs and stores the calculated sgpa along with USN and Name in a csv file.

The script uses Selenium webdriver and BeautifulSoup to scrape data from webpage.

You need to have the required libraries installed on your machine to run the script.

You can install the libraries using the command:
pip install "library-name"

Script also requires you to download the Chrome webdriver, you can download it from : https://sites.google.com/a/chromium.org/chromedriver/downloads

# Steps to configure the Chrome-webdriver in the script:
1. Install the webdriver and copy the location of the path where the chromedriver was installed.

2. Now,change the value of "executable_path" to the path you just copied. (line 29)

# Modifying the program
Provide the last valid USN to the variable "last". (line 25)

Change the college code in "usn". (line 32)
