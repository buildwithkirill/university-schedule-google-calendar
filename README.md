University Schedule → Google Calendar

Automatically sync university schedule data from the Herzen University website into Google Calendar.

Features
Scrapes the latest university schedule
Parses classes, teachers, classrooms, and dates
Exports schedule data to JSON
Automatically updates Google Calendar
Removes outdated events before synchronization
Prevents duplicate events
Supports a dedicated university calendar
Tech Stack
Python
Requests
BeautifulSoup4
Google Calendar API
JSON
Git
Project Structure
schedule.py          - Schedule parser
import_calendar.py   - Google Calendar synchronization
main.py              - Full automation workflow
schedule.json        - Parsed schedule data

Installation

Install dependencies:

pip install requests
pip install beautifulsoup4
pip install google-api-python-client
pip install google-auth-oauthlib
pip install google-auth-httplib2

Usage

Run:

python main.py


The script will:

Download the latest schedule
Generate a JSON file
Clear the target calendar
Upload fresh events
Security

The following files are excluded from Git:

credentials.json
token.json


These files contain authentication credentials and should never be committed.

Future Improvements
Incremental schedule updates
Support for multiple groups
Docker support
Telegram notifications
Better event comparison logic
Author

Built by Kirill (@buildwithkirill)

A personal project focused on:

Web Scraping
JSON Processing
OAuth Authentication
Google Calendar API
Automation
