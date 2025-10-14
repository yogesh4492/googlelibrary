from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

source=['https://www.googleapis.com/auth/drive']
flow= InstalledAppFlow.from_client_secrets_file('credentials.json',source)
creds=flow.run_local_server(port=0)
service=build('drive','v3',credentials=creds)

file_id = '1CQGKqUpYB7zBoVla9B0Ijy4YUK_rPGeR'
request = service.files().get_media(fileId=file_id)
fh = io.FileIO('downloaded.txt', 'wb')

downloader = MediaIoBaseDownload(fh, request)
done = False

while not done:
    status, done = downloader.next_chunk()
    print(f"Download {int(status.progress() * 100)}%.")