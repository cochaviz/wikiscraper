# wikiscraper
Wikipedia scraper for the terminal

### Installation
Give the program the appropriate permissions:

`chmod +x ./wikiscraper.py`

### Dependencies
Some 3rd party packages are required for the wikiscraper to work
 - urllib
 - bs4
 - lxml

Ubuntu: `pip3 install urllib3 bs4 lxml`

Otherwise: `pip install urllib3 bs4 lxml`

> If you don't use pip, good luck!

### Usage
```
 -s                     List sources
 -h --help              Show this help
 -S --search            Search for a specific article
 -U --url               Enter a full url to scrape (can also be a non-wikipedia url, will look for <p> tags)
 ```
