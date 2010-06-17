from django.db import models


class Bucket(models.Model):
    """
    Data about the ``bucket`` object on Amazon S3.

    - name
    - acl
    - logging
    -
    """
    pass


class Key(models.Model):
    """
    Represents a single Amazon S3 object.

    - bucket
    - name
    - acl
    - size
    - md5
    - last_modified
    """
    pass


class MetaData(models.Model):
    """
    Represents a single meta data key value pair associated with an object.
    """
    pass