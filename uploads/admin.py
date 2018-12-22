from django.contrib import admin
from .models import UploadType1, UploadType2
from drf_chunked_upload.admin import ChunkedUploadAdmin

admin.site.register(UploadType1, ChunkedUploadAdmin)
admin.site.register(UploadType2, ChunkedUploadAdmin)
