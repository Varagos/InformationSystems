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
