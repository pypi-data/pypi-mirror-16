Throwie
===================
A small CLI tool aimed to simplify EC2 tags management

----

Throwie - creates or updates tags on a filtered collection of EC2 instances. In a nutshell it:

* Filters instances based on specified criteria
* Removes existing tags from filtered collection (if required)
* Creates new tags on filtered collection of EC2 instances

Usage
-----------------
::

    usage: throwie [-h] -f FILTER_TYPE -i INVENTORY [INVENTORY ...] -t TAGS

    Throwie - create/update tags on a collection of EC2 instances.

    optional arguments:
      -h, --help            show this help message and exit
      -f FILTER_TYPE, --filter_type FILTER_TYPE EC2 filter type, see EC2.Client.describe_instances for valid filter values
      -i INVENTORY [INVENTORY ...], --inventory INVENTORY [INVENTORY ...] EC2 filter values, space separated, could be private ip addresses or instance-id depending on filter type
      -t TAGS, --tags TAGS  EC2 tags in json format


Installation
-----------------

::

    $ pip install throwie


Example
-------------------
Tag EC2 instances by specified private ip addresses:

::

    throwie -i 192.168.244.192 192.168.247.118 -f private-ip-address --tags '{"api-version": "v1.0.1"}'

Tag EC2 instances by specified instance ids:

::

    throwie -i i-cex0d811 i-561s6370 -f instance-id --tags '{"api-version": "v1.0.1"}'


