# Examples on how to work with IPSec Tunnels
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

## List all IPSec Tunnels
By default, it will list all IPSec Tunnels in the _Service Connections_ folder.
```python
o = serviceSetup.serviceSetup(n)

o.paIpsecTunnelsListIpsecTunnels()
```

To list all IPSec Tunnels in _Remote Networks_ folder: 
```python
o = serviceSetup.serviceSetup(n)

o.paIpsecTunnelsListIpsecTunnels("Remote Networks")
```

## Create an IPSec Tunnel
To create an _IPSec Tunnel_
```python
o = serviceSetup.serviceSetup(n)

# Ensure that any referenced objects e.g. ike_gateway are created first.
ipsecTunnel = { "name": "Docker_Net2", "tunnel_interface": "tunnel", "auto_key": { "ike_gateway": [ { "name":  "ike_Gateway_1631893679042" } ], "ipsec_crypto_profile": "Others-IPSec-Crypto-Default" }, "tunnel_monitor": { "enable": True, "destination_ip": "192.168.1.1" }, "anti_replay": True }
o.paIpsecTunnelsCreateIpsecTunnel(ipsecTunnel)
```

## Edit a IPSec Tunnel
To edit an existing _IPSec Tunnel_. 

The name property in the json should reflect the actual name of the IPSec Tunnel. Does not support renaming tunnel (yet)

```python
o = serviceSetup.serviceSetup(n)

ipsecTunnel = { "name": "Docker_Net2", "tunnel_interface": "tunnel", "auto_key": { "ike_gateway": [ { "name":  "ike_Gateway_1631893679042" } ], "ipsec_crypto_profile": "Others-IPSec-Crypto-Default" }, "tunnel_monitor": { "enable": True, "destination_ip": "192.168.1.2" }, "anti_replay": True }
o.paIpsecTunnelsEditIpsecTunnel(ipsecTunnel)
```

## Delete a Service Connection
To delete an _IPSec Tunnel_ in the _Remote Networks_ folder. 

```python
o = serviceSetup.serviceSetup(n)

ipsecTunnel = { "name": "Docker_Net3" }
o.paIpsecTunnelsDeleteIpsecTunnel(ipsecTunnel, "Remote Networks")
```