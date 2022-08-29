# InformationSystems

## ArangoDB

### Ubuntu 20.04 -

https://www.arangodb.com/download-major/ubuntu/
(via package manager)

- sudo apt update
- sudo apt install curl apt-transport-https gnupg2 -y

First add the repository key to apt like this:

```bash
curl -OL https://download.arangodb.com/arangodb39/DEBIAN/Release.key
sudo apt-key add - < Release.key
```

Add the ubuntu repository

```bash
echo 'deb https://download.arangodb.com/arangodb39/DEBIAN/ /' | sudo tee /etc/apt/sources.list.d/arangodb.list
```

Refresh apt

```bash
sudo apt update
```

Install arangodb by running

```bash
sudo apt install arangodb3=3.9.2-1
```

Check status

```
sudo systemctl status arangodb3
```

Enable the WEB UI  
for data-configuring the instance etc

```bash
vim /etc/arangodb3/arangod.conf

# Replace the line of endpoint = tcp.. , with
# endpoint = tcp://ip-server-of-server-or-domain:8529
# Save changes and restart the arangodb service

sudo systemctl restart arangodb3
```

For this to work we need to open port 8529 on our vm(vps provider)

## Usage

ArangoDB can be used as a graph db, a document db or a key-value store db.  
Can be used as an elastic search replacement(for search)  
builtin-fox javascript framework for nodejs microservices (with great performance)  
Good for geo-spacial searches also. Natively supports polygon searches.

```bash
docker run -e ARANGO_NO_AUTH=1 -p 8529:8529 -d --name test-arangodb arangodb
```

Visit localhost:8529  
Create a collection named friends

```js
insert { name: "Will" } into friends
// Cmd+Enter to run query
// Key is like a primary id
return document("friends/151")
return document(["friends/514", "friends/122"])

for friend in friends
    return friend

for friend in friends
    filter friend.name == "Will"
    // filter friend.age > 5
    return friend

// Join
for friend in friends
    for state in states
    filter friend.state == state._key
    // Return anything we like
    return {friend, state: state.name}
```

### Use it as key-value

Create a collection names sessions

```js
insert {_key: "abcde", logins: 1} into sessions

// Simply fetch it since we have specified the key
return document("sessions/abcde");
```

## Usage with arangosh(shell client)

https://www.arangodb.com/docs/stable/programs-arangosh.html

python2.7 ./bin/ycsb load arangodb -s -P workloads/workloada -p arangodb.ip="localhost" -p arangodb.port=8529

## Riak KV

Riak KV is a distributed key-value NoSQL database designed to deliver maximum data availability by distributing data across multiple servers. As long as your Riak KV client can reach one Riak server, it should be able to write data.

```bash
cd riak

docker-compose up -d coordinator

# navigate to http://localhost:8098/admin/
# https://docs.riak.com/riak/kv/latest/using/admin/riak-control/index.html
# read more https://hub.docker.com/r/basho/riak-kv/
```

_Chose Riak® KV flexible key-value data model for web scale profile and session management, real-time big data, catalog, content management, customer 360, digital messaging, and more use cases._  
[Riak KV Tour](https://riak.com/products/riak-kv/resiliency/index.html?p=10906.html)

## YCSB

https://github.com/brianfrankcooper/YCSB
