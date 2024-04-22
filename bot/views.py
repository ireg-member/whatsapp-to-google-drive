import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from twilio.rest import Client
from django.conf import settings
from bot.models import MyDrive
from bot.utilities import create_user_directory, list_directories, upload_file_to_drive


account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
client = Client(account_sid, auth_token)
google_access_token = settings.GOOGLE_ACCESS_TOKEN


class ImageStoreView(APIView):

    def post(self, request):

        media_type = request.POST["MediaContentType0"]
        if media_type in ["image/png", "image/jpeg", "image/gif", "image/webp", "image/tiff", "image/psd", "image/eps", "image/indd", 'image/ai']:
            media_url = request.POST["MediaUrl0"]
            media_sid = request.POST['MessageSid']
            if media_sid is not None:
                media_sid = media_sid + "." + media_type.split('/')[-1]
            directory_name = request.POST["From"]
            file_name = request.POST["MediaUrl0"].split("/")[-1]
            try:
                drive = MyDrive.objects.get(drive_name=directory_name, drive_id__isnull=False)
            except:
                drive = MyDrive.objects.create(drive_name=directory_name)
                drive_id = create_user_directory(google_access_token, directory_name)
                drive.drive_id = drive_id
                drive.save()
            response = upload_file_to_drive(google_access_token, media_url, media_sid, file_name, drive.drive_id)
            if response["status"] == 200:
                client.messages.create(
                        from_='whatsapp:+14155238886',
                        body="Your Image has been stored!",
                        to=request.POST["From"]
                    )
                return Response({"message": "Your Image has been stored!"})
            client.messages.create(
                from_='whatsapp:+14155238886',
                body="Please send your image here!",
                to=request.POST["From"]
            )
            return Response({"message": "Something went wrong!"})

