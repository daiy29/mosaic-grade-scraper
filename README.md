# Mosaic Mark Scraper

Mosaic Mark Scraper is a simple script made in Python that periodically checks the McMaster website every 60 seconds and sends the user an e-mail if there are updates. Instructions are for a Windows system.

## Requirements

This script requires [Python](https://www.python.org/downloads/), [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), as well as [requests](https://pypi.org/project/requests/) to be installed. 

```sh
pip install beautifulsoup4
```

```sh
python -m pip install requests
```
## Usage

Save the scraper.py file, cd into the directory it is saved.
The script can be run with scraper.py arg1 arg2 arg3 arg4, where
- arg1 should be replaced by your Mosaic username
- arg2 should be replaced by your Mosaic password
- arg3 should be replaced by your Gmail username
- arg4 should be replaced by your Gmail password

Prior to using the script, critical security alerts for less secure apps on Gmail should be disabled. Instructions can be found [here](https://hotter.io/docs/email-accounts/secure-app-gmail/), under the second category. The script will still work regardless, but e-mails may be blocked.

