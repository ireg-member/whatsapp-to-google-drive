from django.db import models


class MyDrive(models.Model):
    drive_id = models.CharField(max_length=255)
    drive_name = models.CharField(max_length=100)
    text_file_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.drive_name

    class Meta:
        verbose_name = "MyDrive"
        verbose_name_plural = "MyDrives"


