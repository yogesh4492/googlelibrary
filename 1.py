from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import io
import os
import typer
import json
import csv


scope=['https://www.googleapis.com/auth/drive']


flow=InstalledAppFlow.from_client_secrets_file('credentials.json',scope)

creds=flow.run_local_server(port=0)


service = build('drive','v3',credentials=creds)


