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
./bin/ycsb load arangodb -s -P workloads/workloada -p recordcount=500000 -threads 16 -p arangodb.ip=arango-host -p arangodb.port=8529 -p arangodb.dropDBBeforeRun=true
```

Then, run the workload:

```bash
./bin/ycsb run arangodb -s -P workloads/workloada -p operationcount=500000 -threads 1 -p arangodb.ip=arango-host -p arangodb.port=8529

# Or with target
./bin/ycsb run arangodb -s -P workloads/workloadb -p operationcount=20000 -threads 64 -p target=2000 -p arangodb.ip=arango-host -p arangodb.port=8529
```
