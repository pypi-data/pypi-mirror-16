[![Build Status](https://travis-ci.org/datamountaineer/python-serializers.svg?branch=master)](https://travis-ci.org/datamountaineer/python-serializers)

# Python Schema Registry Client and Serializers/Deserializers

A Python client used to interact with [Confluent](http://confluent.io/)'s
[schema registry](https://github.com/confluentinc/schema-registry).  Supports Python 3.5.  This also works within a virtual env.

The API is heavily based off of the existing Java API of [Confluent schema registry](https://github.com/confluentinc/schema-registry).

The serializers/deserializers use [fastavro](https://github.com/tebeka/fastavro) for reading and writing.

# Installation

Run `python setup.py install` from the source root.


# Example Usage

Setup

```python
from datamountaineer.schemaregistry.client import CachedSchemaRegistryClient
from datamountaineer.schemaregistry.serializers import MessageSerializer, Util

# Initialize the client
client = CachedSchemaRegistryClient(url='http://registry.host')
```

Schema operations

```python
# register a schema for a subject
schema_id = client.register('my_subject', avro_schema)

# fetch a schema by ID
avro_schema = client.get_by_id(schema_id)

# get the latest schema info for a subject
schema_id,avro_schema,schema_version = client.get_latest_schema('my_subject')

# get the version of a schema
schema_version = client.get_version('my_subject', avro_schema)

# Compatibility tests
is_compatible = client.test_compatibility('my_subject', another_schema)

# One of NONE, FULL, FORWARD, BACKWARD
new_level = client.update_compatibility('NONE','my_subject')
current_level = client.get_compatibility('my_subject')
```

Encoding to write back to Kafka. Encoding by id is the most efficent as it avoids an extra trip to the Schema Registry to
lookup the schema id.

```python
# Message operations

# encode a record to put onto kafka
serializer = MessageSerializer(client)

#build your avro
record = get_obj_to_put_into_kafka()

# use the schema id directly
encoded = serializer.encode_record_with_schema_id(schema_id, record)
```

Encode by schema only.

```python
# use an existing schema and topic
# this will register the schema to the right subject based
# on the topic name and then serialize
encoded = serializer.encode_record_with_schema('my_topic', avro_schema, record)
```

Reading messages

```python
# decode a message from kafka
message = get_message_from_kafka()
decoded_object = serializer.decode_message(message)
```

# License

The project is licensed under the Apache 2 license.
