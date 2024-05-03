from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PDFFile
from .serializers import PDFFileSerializer
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os



@api_view(['POST'])
def upload_pdf_file(request):
    if request.method == 'POST':
        serializer = PDFFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def list_uploaded_pdf(request):
    if request.method == 'GET':
        pdf_files = PDFFile.objects.all()
        serializer = PDFFileSerializer(pdf_files, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])        
def download_pdf(request, pdf_id):
    if request.method == 'GET':
        pdf_file = get_object_or_404(PDFFile, pk=pdf_id)
        file_path = os.path.join(settings.MEDIA_ROOT, str(pdf_file.file))
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')  

