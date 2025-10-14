from  google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


source=['https://www.googleapis.com/auth/drive']

flow=InstalledAppFlow.from_client_secrets_file('credentials.json',source)

creds=flow.run_local_server(port=0)

service =  build('drive','v3',credentials=creds)

file_metadata={'name':'topic.txt'}
media=MediaFileUpload('topic.txt',mimetype='text/plain')

file=service.files().create(
    body=file_metadata,
    media_body=media,
    fields='name,id'
).execute()

print(f"File Uploaded folder id is ({file})")