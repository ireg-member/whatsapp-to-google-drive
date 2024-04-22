import requests
import json
from django.conf import settings
from requests.auth import HTTPBasicAuth
from rest_framework import status
import os


def create_user_directory(access_token, directory_name):
    # URL for creating folders in Google Drive
    create_folder_url = 'https://www.googleapis.com/drive/v3/files'

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Metadata for the folder
    folder_metadata = {
        'name': directory_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    response = requests.post(create_folder_url, headers=headers, data=json.dumps(folder_metadata))

    if response.status_code == 200:
        folder_id = response.json().get('id')
        return folder_id
    else:

        return None


def list_directories(access_token):
    # URL for listing files (folders) in Google Drive
    list_files_url = 'https://www.googleapis.com/drive/v3/files'

    # Headers containing authorization token
    headers = {
        'Authorization': 'Bearer ' + access_token
    }

    # Query parameters to filter for folders
    params = {
        'q': "mimeType='application/vnd.google-apps.folder'",  # Filter for folders
        'fields': 'files(id, name)'  # Specify fields to include in the response
    }

    # Make a GET request to list folders
    response = requests.get(list_files_url, headers=headers, params=params)

    if response.status_code == 200:
        folders = response.json().get('files', [])
        for folder in folders:
            print(f"Folder ID: {folder['id']}, Name: {folder['name']}")
    else:
        print("Failed to list folders. Status code:", response.status_code)
        print("Error message:", response.text)


def upload_file_to_drive(access_token, media_url, media_sid, file_name, directory_id):
    # URL for uploading files to Google Drive
    upload_url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'

    headers = {
        'Authorization': 'Bearer ' + access_token
    }

    para = {
        "name": file_name,
        "parents": [directory_id]
    }

    file = download_file(media_url, media_sid)

    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(file, 'rb')
    }

    response = requests.post(upload_url, headers=headers, files=files)

    if response.status_code == 200:
        return {"message": "File uploaded successfully!", "status": status.HTTP_200_OK}
    else:
        return {"message": "Failed to upload file", "status": status.HTTP_400_BAD_REQUEST}


def download_file(media_url, media_sid):
    response = requests.get(media_url, auth=HTTPBasicAuth(settings.TWILIO_ACCOUNT_SID, settings.AUTH_TOKEN), stream=True)

    if response.status_code == 200:
        image_directory = os.path.join(settings.MEDIA_ROOT, 'images')

        if not os.path.exists(image_directory):
            os.makedirs(image_directory)
        image_path = os.path.join(image_directory, f'{media_sid}')

        with open(f'{image_path}', 'wb') as f:  # Save the image file
            for chunk in response:
                f.write(chunk)
        return image_path
