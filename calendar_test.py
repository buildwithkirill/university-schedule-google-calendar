from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    SCOPES
)

print("Старт")

creds = flow.run_local_server(port=0)

print("После авторизации")

service = build(
    "calendar",
    "v3",
    credentials=creds
)
event = {
    "summary": "Тестовая пара",
    "location": "РГПУ Герцен",
    "start": {
        "dateTime": "2026-11-09T08:15:00",
        "timeZone": "Asia/Tashkent",
    },
    "end": {
        "dateTime": "2026-11-09T09:45:00",
        "timeZone": "Asia/Tashkent",
    },
}
service.events().insert(
    calendarId="primary",
    body=event
).execute()
print("Шаг 3")

result = service.calendarList().list().execute()

print("Шаг 4")

for calendar in result["items"]:
    print(calendar["summary"])

print("Успешно!")
