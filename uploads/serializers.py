from drf_chunked_upload.serializers import (
    ChunkedUploadSerializer,
    ChunkedUploadCreatedSerializer
)
from .models import UploadType1, UploadType2


class UploadType1Serializer(ChunkedUploadSerializer):
    viewname = 'uploads:upload-type-1-detail'

    class Meta(ChunkedUploadSerializer.Meta):
        model = UploadType1


class UploadType1CreatedSerializer(ChunkedUploadCreatedSerializer):
    viewname = 'uploads:upload-type-1-detail'

    class Meta(ChunkedUploadCreatedSerializer.Meta):
        model = UploadType1


class UploadType2Serializer(ChunkedUploadSerializer):
    viewname = 'uploads:upload-type-2-detail'

    class Meta(ChunkedUploadSerializer.Meta):
        model = UploadType2


class UploadType2CreatedSerializer(ChunkedUploadCreatedSerializer):
    viewname = 'uploads:upload-type-2-detail'

    class Meta(ChunkedUploadCreatedSerializer.Meta):
        model = UploadType2
