from django.urls import path
# from .views import PDFUploadView, PDFListView
from.import views

urlpatterns = [
#     path('upload/', PDFUploadView.as_view(), name='pdf-upload'),
#     path('list/', PDFListView.as_view(), name='pdf-list'),
path('upload_pdf_file/', views.upload_pdf_file),
path('list_uploaded_pdf/', views.list_uploaded_pdf),
path('download_pdf/<int:pdf_id>/', views.download_pdf),
]