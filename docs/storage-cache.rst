----------------------------
Simple Storage Service Cache
----------------------------

This app has one or more models, a management command, and set of default
date based views.

The idea is simple.  It's far too expensive to iterate over any decent size
S3 bucket, however, it is generally useful to know what's out there on your
slice of the cloud.  By leveraging a local data store, you can have an up 
to date cache of files, their meta data, and their object url.

More to come on this later...