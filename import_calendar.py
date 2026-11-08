import json

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    SCOPES
)

creds = flow.run_local_server(port=0)

service = build(
    "calendar",
    "v3",
    credentials=creds
)

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
        calendarId="primary",
        body=event
    ).execute()

    print("Пара добавлена!")