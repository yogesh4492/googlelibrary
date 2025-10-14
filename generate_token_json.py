from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes define permissions (Drive read/write)
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    creds = None

    # 1️⃣ Check if token.json already exists
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # 2️⃣ If no valid creds available, log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh automatically if expired
            creds.refresh(Request())
        else:
            # Authenticate manually (only first time)
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # 3️⃣ Build Drive service
    service = build('drive', 'v3', credentials=creds)

    # 4️⃣ Example: list 5 files
    results = service.files().list(
        pageSize=5, fields="files(id, name)"
    ).execute()

    items = results.get('files', [])
    if not items:
        print("No files found.")
    else:
        for item in items:
            print(f"{item['name']} ({item['id']})")

if __name__ == '__main__':
    main()
