# Examples on how to work with IKE Gateways
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

## List all IKE Gateways
By default, it will list all IKE Gateways in the _Service Connections_ folder.
```python
o = serviceSetup.serviceSetup(n)

o.paIkeGatewaysListIkeGateways()
```

To list all IKE Gateways in _Remote Networks_ folder: 
```python
o = serviceSetup.serviceSetup(n)

o.paIkeGatewaysListIkeGateways("Remote Networks")
```

## Create an IKE Gateways
To create an _IKE Gateways_
```python
o = serviceSetup.serviceSetup(n)

ikeGateway = {"name": "TestGateway1", "peer_address": {"dynamic": {}}, "authentication": {"pre_shared_key": {"key": "examplekey1234"}}, "local_id": {"type": "fqdn", "id": "prismaaccess1234.local"}, "peer_id": {"type": "fqdn", "id": "remotebranch1234.pj.local"}, "protocol": {"ikev1": {"ike_crypto_profile": "CloudGenix-IKE-Crypto-Default", "dpd": {"enable": True}}, "ikev2": {"dpd": {"enable": True}}}}
o.paIkeGatewaysCreateIkeGateway(ikeGateway)
```

## Edit a IKE Gateways
To edit an existing _IKE Gateways_. 

The name property in the json should reflect the actual name of the IKE Gateways. Does not support renaming tunnel (yet)

```python
o = serviceSetup.serviceSetup(n)

ikeGateway = {"name": "TestGateway1", "peer_address": {"dynamic": {}}, "authentication": {"pre_shared_key": {"key": "examplekey1234"}}, "local_id": {"type": "fqdn", "id": "pr1234ismaaccess1234.local"}, "peer_id": {"type": "fqdn", "id": "remo1234tebranch1234.pj.local"}, "protocol": {"ikev1": {"ike_crypto_profile": "CloudGenix-IKE-Crypto-Default", "dpd": {"enable": True}}, "ikev2": {"dpd": {"enable": True}}}}
o.paIkeGatewaysEditIkeGateway(ikeGateway)
```

## Delete a IKE Gateways
To delete an _IKE Gateways_ in the _Remote Networks_ folder. 

```python
o = serviceSetup.serviceSetup(n)

ikeGateway = { "name": "TestGateway1" }
o.paIkeGatewaysDeleteIkeGateway(ikeGateway, "Remote Networks")
```