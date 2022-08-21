Download
https://stackoverflow.com/questions/71975162/how-do-i-install-riak-on-ubuntu-using-apt  
from https://files.tiot.jp/riak/kv/3.0/3.0.10/ubuntu/focal64/

riak.config under /etc/riak

The unique thing about Riak is not the typical master slave model. Riak stores key-values into a bucket then the bucket and key are hashed together which maps the result to a 160 bit integer space. Riak then divides this space into partitions which are managed by virtual nodes. Physical nodes then divide up the virtual nodes among themselves. The way Riak does implicit data replication is that when you write data to one of these virtual partitions it is automatically copied to n more partitions that are adjacent to the written one.

```
riak admin bucket-type create maps '{"props": {"datatype": "map"}}'
```
