# Template Tags for django-aws	

Before using any of these tags in your templates, remember to load them with
`{% load aws %}`.

## Tags for S3

Tags for Amazon's storage service, S3, will allow you to list buckets, 
enumerate the contents of a bucket, and display information about a particular
object.

### `get_buckets`

Gets a list of bucket objects.

Syntax:

    {% get_buckets as [varname] %}

Example:

    {% get_buckets as buckets %}


### `list_bucket`

Gets a list of objects inside a particular bucket.

Syntax:

	{% list_bucket [bucket_name] [prefix] as [varname] %}
	
Example:

	{% list_bucket example.com images as image_list %}
	

### `get_object_info`

Gets information about a particular object.

Syntax:

	{% get_object_info [bucket_name] [key_name] as [varname] %}
	
Example:

	{% get_object_info example.com images/2008/07/01/cool.png as image %}


## Tags for EC2

Tags for Amazon's elastic compute cloud service, that will allow you to list 
running machines and various details about them.

### `get_running_nodes`

### `get_node_info`


## Tags for SQS

Tags for Amazon's message queueing service that will provide information to 
the template context such as listing available queues and their estimated 
count of messages.

### `get_queues`

### `get_message_count`


