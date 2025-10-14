from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build



scope=['https://www.googleapis.com/auth/drive']

flow=InstalledAppFlow.from_client_secrets_file('credentials.json',scope)

creds=flow.run_local_server(port=0)

# print(creds)

service =  build('drive','v3',credentials=creds)


result=service.files().list(
    pageSize=10,fields='files(id,name)'
).execute()


print("Files:")
for item in result['files']:
    print(f"{item['name']} ({item['id']})")