from django.utils.deconstruct import deconstructible
from uuid import uuid4
import os
from django.utils.crypto import get_random_string


def rename_upload(path):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        unique_id = str(get_random_string(length=50))
        if instance.pk:
            filename = "{}{}.{}".format(instance.pk, unique_id, ext)
        else:
            filename = "{}{}.{}".format(uuid4().hex, unique_id, ext)

        return os.path.join(path, filename)

    return wrapper
