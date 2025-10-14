from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

scope=['https://www.googleapis.com/auth/drive']

flow=InstalledAppFlow.from_client_secrets_file('credentials.json',scope)

creds=flow.run_local_server(port=0)

service = build('drive','v3',credentials=creds)
