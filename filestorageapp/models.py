from django.db import models
import datetime


class PDFFile(models.Model):
    file = models.FileField(upload_to='file/')
    uploaded_at = models.DateTimeField(default=datetime.datetime.now)