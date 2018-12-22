from django.urls import re_path
from drf_chunked_upload.urls import PK_QUERY
from .views import UploadType1View, UploadType2View

urlpatterns = [
    re_path(r'^upload-type-1/$', UploadType1View.as_view(), name='upload-type-1-list'),
    re_path(r'^upload-type-1/{}/$'.format(PK_QUERY), UploadType1View.as_view(), name='upload-type-1-detail'),
    re_path(r'^upload-type-2/$', UploadType2View.as_view(), name='upload-type-2-list'),
    re_path(r'^upload-type-2/{}/$'.format(PK_QUERY), UploadType2View.as_view(), name='upload-type-2-detail'),
]
