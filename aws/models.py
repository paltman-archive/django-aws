from django.db import models

class StorageObject(models.Model):
    """Represents a single Amazon S3 object."""
    pass


class MetaData(models.Model):
    """Represents a single meta data key value pair associated with an object."""
    pass