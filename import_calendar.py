import json
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
CALENDAR_ID = "65c067decea67c9f2b6f34b09fa346b25d13717fceb9b681035e0135987cf892@group.calendar.google.com"
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        SCOPES
    )

if not creds:
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())


service = build(
    "calendar",
    "v3",
    credentials=creds
)
events = service.events().list(
    calendarId=CALENDAR_ID
).execute()

for event in events.get("items", []):
    try:
        service.events().delete(
            calendarId=CALENDAR_ID,
            eventId=event["id"]
        ).execute()
    except Exception:
        pass

print("Календарь очищен")

with open(
    "schedule.json",
    "r",
    encoding="utf-8"
) as file:

    lessons = json.load(file)


for lesson in lessons:

    date = lesson["date"].split(",")[0]
    times = lesson["time"].split("-")

    start_time = times[0]
    end_time = times[1]
    parts = date.split(".")

    day = parts[0].zfill(2)
    month = parts[1].zfill(2)
    year = parts[2]

    start_datetime = f"{year}-{month}-{day}T{start_time}:00"
    end_datetime = f"{year}-{month}-{day}T{end_time}:00"

    print(start_datetime)
    print(end_datetime)
    event = {
        "summary": lesson["lesson"],
        "location": lesson["room"],
        "description": lesson["teacher"],
        "start": {
            "dateTime": start_datetime,
            "timeZone": "Asia/Tashkent"
        },
        "end": {
            "dateTime": end_datetime,
            "timeZone": "Asia/Tashkent"
        }
    }
    service.events().insert(
        calendarId=CALENDAR_ID,
        body=event
    ).execute()

    print("Пара добавлена!")