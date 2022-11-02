# Examples on how to work with Service Connections
In all examples, it will either return a success or failure when attempting the operation.

## Authentication
First authenticate to the API service:
```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```

Now we can proceed with the commands below.

## List all Service Connections
```python
o = serviceSetup.serviceSetup(n)

o.paServiceConnectionsListServiceConnections()
```


## Create an Service Connection
To create an _Service Connection_
```python
o = serviceSetup.serviceSetup(n)

ServiceConnection1 = { "name": "ServiceConnection1", "region": "us-west-2", "ipsec_tunnel": "Docker_Net", "subnets": [ "192.168.199.0/24" ] }

o.paServiceConnectionsCreateServiceConnection(ServiceConnection1)
```

## Edit a Service Connection
To edit an existing _Service Connection_. 

The name property in the json should reflect the actual name of the service connection.

Once a service connection has been created, you cannot edit the name. You have to delete and add a new service connection.
```python
o = serviceSetup.serviceSetup(n)

ServiceConnection1 = { "name": "ServiceConnection1", "region": "us-west-2", "ipsec_tunnel": "Docker_Net", "subnets": [ "192.168.190.0/24" ] }

o.paServiceConnectionsEditServiceConnection(ServiceConnection1)
```

## Delete a Service Connection
To edit an delete a _Service Connection_. 

```python
o = serviceSetup.serviceSetup(n)

ServiceConnection1 = { "name": "ServiceConnection1" }

o.paServiceConnectionsDeleteServiceConnection(ServiceConnection1)
```