First, drop the existing collection: "usertable" under database "ycsb":

```bash
# If system arango is running
# On arango-host
arangosh
# Empty password
db._useDatabase("ycsb")
# db._collections()
db._collection("usertable").drop()
```

Then, load the data:

```bash
./bin/ycsb load arangodb -s -P workloads/workloada -p arangodb.ip=arango-host -p arangodb.port=8529
```

Then, run the workload:

```bash
./bin/ycsb run arangodb -s -P workloads/workloada -p arangodb.ip=arango-host -p arangodb.port=8529
```
