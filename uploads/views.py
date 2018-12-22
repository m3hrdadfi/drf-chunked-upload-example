from drf_chunked_upload.views import ChunkedUploadView
from .models import UploadType1, UploadType2
from .serializers import (
    UploadType1Serializer,
    UploadType1CreatedSerializer,
    UploadType2Serializer,
    UploadType2CreatedSerializer,
)


class UploadType1View(ChunkedUploadView):
    model = UploadType1
    serializer_class = UploadType1Serializer
    max_bytes = UploadType1.MAX_BYTES

    @property
    def response_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request is None or self.request.method not in ['PUT', 'POST']:
            serializer_class = UploadType1CreatedSerializer
        return serializer_class


class UploadType2View(ChunkedUploadView):
    model = UploadType2
    serializer_class = UploadType2Serializer
    max_bytes = UploadType2.MAX_BYTES

    @property
    def response_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request is None or self.request.method not in ['PUT', 'POST']:
            serializer_class = UploadType2CreatedSerializer
        return serializer_class
