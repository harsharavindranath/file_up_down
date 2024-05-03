# Generated by Django 5.0.4 on 2024-05-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filestorageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pdfs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Files',
        ),
    ]
