iownload
https://stackoverflow.com/questions/71975162/how-do-i-install-riak-on-ubuntu-using-apt  
from https://files.tiot.jp/riak/kv/3.0/3.0.10/ubuntu/focal64/

riak.config under /etc/riak

The unique thing about Riak is not the typical master slave model. Riak stores key-values into a bucket then the bucket and key are hashed together which maps the result to a 160 bit integer space. Riak then divides this space into partitions which are managed by virtual nodes. Physical nodes then divide up the virtual nodes among themselves. The way Riak does implicit data replication is that when you write data to one of these virtual partitions it is automatically copied to n more partitions that are adjacent to the written one.

```
riak admin bucket-type create maps '{"props": {"datatype": "map"}}'
```

# Riak -YCSB

```bash
# Dependencies java1.6+., maven
# Skip these steps if you already have java & maven
sudo apt update

sudo apt install default-jre
java -version

sudo apt install default-jdk
javac -version

sudo apt install maven

# Bootstrap Riak-kv simple node
docker run --name=riak -d -p 8087:8087 -p 8098:8098 basho/riak-kv

docker exec -it riak sh
vi /etc/riak/riak.conf
# Set
# storage_backend = leveldb
# Close container shell
docker restart riak

# These may take some seconds
docker exec -it riak sh
riak-admin bucket-type create ycsb '{"props":{"allow_mult":"false"}}'
riak-admin bucket-type activate ycsb

# Load and run a YCSB workload using the Riak client:
./bin/ycsb load riak -P workloads/workloada
./bin/ycsb run riak -P workloads/workloada

# Riak listens on 8098 for HTTP and 8087-Protocol Buffer
# The default protocol buffer riak port will be used (8087)
# The http port (8098) is used for dashboard & commands

# to use params
./bin/ycsb load riak -P workloads/workloada -p recordcount=500000 -threads 16 -P ./path/to/propsFile

./bin/ycsb run riak -P workloads/workloada -p operationcount=20000 -threads 64 -p target=2000 -P ./path/to/propsFile

```

## Riaks props file

```text
riak.hosts=127.0.0.1
riak.port=8098
riak.r_val=1
riak.w_val=1
riak.read_retry_count=2
riak.wait_time_before_retry=1
riak.bucket_type=ycsb
riak.strong_consistency=false
riak.debug=true
```

Refs

- [Riak docker-cluster-config instructions](https://riak.com/posts/technical/running-riak-in-docker/index.html?p=12629.html)
- [Riak advanced config](https://riak.com/posts/technical/running-riak-in-docker/index.html?p=12629.html#:~:text=Advanced%20Configuration)
- [Riak ycsb binding instructions](https://github.com/basho-labs/YCSB/tree/master/riak)
