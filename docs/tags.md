# Template Tags for django-aws

Before using any of these tags in your templates, remember to load them with
``{% load aws %}``.  These tags expose to the template author the following 
boto objects:

 * [S3 Key] (http://boto.googlecode.com/svn/trunk/boto/s3/key.py)
 * [S3 Bucket] (http://boto.googlecode.com/svn/trunk/boto/s3/bucket.py)
 * [EC2 Instance] (http://boto.googlecode.com/svn/trunk/boto/ec2/instance.py)
 * [SQS Queue] (http://boto.googlecode.com/svn/trunk/boto/sqs/queue.py)

## Tags for S3

Tags for Amazon's storage service, S3, will allow you to list buckets, 
enumerate the contents of a bucket, and display information about a particular
object.

### get\_buckets

Gets a list of bucket objects.

Syntax:

    {% get_buckets as [varname] %}

Example:

    {% get_buckets as buckets %}
	<ul>
	{% for bucket in buckets %}
		<li>{{ bucket.name }}</li>
	{% endfor %}
	</ul>


### list\_bucket

Gets a list of objects inside a particular bucket.

Syntax:

	{% list_bucket [bucket_name] [prefix] as [varname] %}
	
Example:

	{% list_bucket example.com images as image_list %}
	<ul>
	{% for key in image_list %}
		<li>{{ key.name }} ({{key.size|filesizeformat}})</li>
	{% endfor %}
	</ul>
	

### get\_object\_info

Gets information about a particular object.

Syntax:

	{% get_object_info [bucket_name] [key_name] as [varname] %}
	
Example:

	{% get_object_info example.com images/2008/07/01/cool.png as image %}
	<ul>
		<li>Name: {{ image.name }}</li>
		<li>Size: {{ image.size|filesizeformat }}</li>
		<li>MD5: {{ image.md5 }}</li>
		<li>Owner: {{ image.owner }}</li>
		<li>Content Type: {{ image.content_type }}</li>
	</ul>


## Tags for EC2

Tags for Amazon's elastic compute cloud service, that will allow you to list 
running machines and various details about them.

### get\_running\_nodes

Syntax:

	{% get_running_nodes as [varname] %}
	
Example:

  	{% get_running_nodes as nodes %}
	<ul>
	{% for node in nodes %}
		<li>{{ node.public_dns_name }}</li>
		<li>{{ node.state }}</li>
		<li>{{ node.launch_time }}</li>
	{% endfor %}
	</ul>

## Tags for SQS

Tags for Amazon's message queueing service that will provide information to 
the template context such as listing available queues and their estimated 
count of messages.

### get\_queues

Syntax:

	{% get_queues as [varname] %}
	
Example:

	{% get_queues as queues %}
	<ul>
	{% for queue in queues %}
		<li>{{ queue.name }} ({{ queue.count }})</li>
	{% endfor %}
	</ul>

### get\_message\_count

Syntax:
	
	{% get_message_count [queue_name] as [varname] %}
	
Example:

	{% get_message_count "myqueue" as queue_count %}
	<p>There are {{ queue_count }} messages in the 'myqueue' queue.</p>





