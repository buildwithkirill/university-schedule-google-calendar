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



result = service.calendarList().list().execute()

for calendar in result["items"]:
    print(calendar["summary"])
    print(calendar["id"])
    print("----------------")

