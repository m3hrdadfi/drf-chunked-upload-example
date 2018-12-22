from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from drf_chunked_upload.models import ChunkedUpload, generate_filename, STORAGE
from drf_chunked_upload.utils import file_cleanup
from drf_chunked_upload.validators import FileValidator

User = get_user_model()


class UploadType1(ChunkedUpload):
    ALLOWED_CONTENT_TYPES = [User]

    def allowed_owners(self):
        return super(UploadType1, self).allowed_owners()

    def allowed_owner(self, owner_type, owner_id=None, msg=None):
        return super(UploadType1, self).allowed_owner(owner_type, owner_id, msg)


class UploadType2(ChunkedUpload):
    ALLOWED_CONTENT_TYPES = [User]
    MIN_BYTES = 0
    MAX_BYTES = 50 * 1024 * 1024
    ALLOWED_EXTENSIONS = None
    ALLOWED_MIMETYPES = ['video/mp4']

    file = models.FileField(
        verbose_name=_('file'),
        max_length=255,
        validators=[FileValidator(min_size=MIN_BYTES,
                                  max_size=MAX_BYTES,
                                  allowed_extensions=ALLOWED_EXTENSIONS,
                                  allowed_mimetypes=ALLOWED_MIMETYPES)],
        upload_to=generate_filename,
        storage=STORAGE,
        null=True)

    def allowed_owners(self):
        return super(UploadType2, self).allowed_owners()

    def allowed_owner(self, owner_type, owner_id=None, msg=None):
        return super(UploadType2, self).allowed_owner(owner_type, owner_id, msg)


@receiver(post_delete, sender=UploadType1)
def auto_file_cleanup(sender, instance, **kwargs):
    file_cleanup(sender, instance, **kwargs)


@receiver(post_delete, sender=UploadType2)
def auto_file_cleanup(sender, instance, **kwargs):
    file_cleanup(sender, instance, **kwargs)
