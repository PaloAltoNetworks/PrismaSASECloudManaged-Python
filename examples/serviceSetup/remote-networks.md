# Examples on how to work with Remote Networks
In all examples, it will either return a success or failure when attempting the operation.

## Authentication
First authenticate to the API service:
```python
from auth import saseAuthentication
from access import prismaAccess
from access import serviceSetup

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```

Now we can proceed with the commands below.

## List all Remote Networks
```python
o = serviceSetup.serviceSetup(n)

o.paRemoteNetworksListRemoteNetworks()
```


## Create an Remote Network
To create an _Remote Network_
```python
o = serviceSetup.serviceSetup(n)

remoteNetwork1 = { "name": "TestRN", "folder": "Remote Networks", "license_type": "FWAAS-AGGREGATE", "region": "us-west-2", "spn_name": "us-northwest-lemon", "ipsec_tunnel": "RN_Site_Tunnel_Pri", "subnets": [ "172.16.0.0/31" ], "protocol": { "bgp": { "enable": True, "peer_as": "65528", "peer_ip_address": "172.16.0.0", "local_ip_address": "172.16.0.1", "originate_default_route": True } }, "ecmp_load_balancing": "disable" }

o.paRemoteNetworksCreateRemoteNetwork(remoteNetwork1)
```

## Edit a Remote Network
To edit an existing _Remote Network_. 

The name property in the json should reflect the actual name of the remote network.

Once a  remote network has been created, you cannot edit the name. You have to delete and add a new remote network.
```python
o = serviceSetup.serviceSetup(n)

remoteNetwork1 = { "name": "TestRN", "folder": "Remote Networks", "license_type": "FWAAS-AGGREGATE", "region": "us-west-2", "spn_name": "us-northwest-lemon", "ipsec_tunnel": "RN_Site_Tunnel1", "subnets": [ "172.16.0.2/31" ], "protocol": { "bgp": { "enable": True, "peer_as": "61100", "peer_ip_address": "172.31.0.1", "local_ip_address": "172.31.0.0", "originate_default_route": True } }, "ecmp_load_balancing": "disable" }

o.paRemoteNetworksEditRemoteNetwork(remoteNetwork1)
```

## Delete a Remote Network
To delete a _Remote Network_. 

```python
o = serviceSetup.serviceSetup(n)

remoteNetwork1 = { "name": "TestRN" }

o.paRemoteNetworksDeleteRemoteNetwork(remoteNetwork1)
```