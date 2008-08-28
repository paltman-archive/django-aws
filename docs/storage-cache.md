# Simple Storage Service Cache

This app has one or more models, a management command, and set of default
date based views.

The idea is simple.  It's far too expensive to iterate over any decent size
S3 bucket, however, it is generally useful to know what's out there on your
slice of the cloud.  By leveraging a local data store, you can have an up 
to date cache of files, their meta data, and their object url.


## The Management Command

The management command seeds the cache with information about your objects
on S3.  The syntax is simple:

    python manage.py syncaws

For this to execute successfully, like just about everything else in this
app, you need boto installed and configured properly.

This command assumes you've already either run syncdb or otherwise have 
already created the tables that correspond to this app's models.  That is
because this command will sync up the table with new/changed data from
your S3 buckets.

## Configuration Settings

Many of settings have defaults, but there are a few that are required.

### AWS_S3_BUCKETS
This setting should be a tuple of all the buckets on your account that 
you are interested in caching to your local data store.

### TODO: DOCUMENT OTHER SETTINGS HERE






