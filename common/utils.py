from django.utils.deconstruct import deconstructible
from uuid import uuid4
import os
from django.utils.crypto import get_random_string


class RenameUpload(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        unique_id = str(get_random_string(length=32))
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = '{}{}.{}'.format(instance.pk,unique_id, ext)
        else:
            filename = '{}{}.{}'.format(uuid4().hex,unique_id, ext)
        return os.path.join(self.path, filename)

