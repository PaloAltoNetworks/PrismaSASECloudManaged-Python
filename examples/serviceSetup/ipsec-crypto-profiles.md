# Examples on how to work with IPSec Crypto Profiles
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

## List all IPSec Crypto Profiles
To list all IPSec Crypto Profiles within shared folder (it defaults to _Service Connections_ folder)
```python
o = serviceSetup.serviceSetup(n)

o.paIpsecCryptoProfilesListIpsecCryptoProfiles()
```


To list all IPSec Crypto Profiles within a specific folder, e.g. _Remote Networks_
```python
o = serviceSetup.serviceSetup(n)

n.paIpsecCryptoProfilesListIpsecCryptoProfiles("Remote Networks")
```


## Create an IPSec Crypto Profile
To create an IPSec Crypto Profile in the _Shared_ folder (it defaults to _Shared_)
```python
o = serviceSetup.serviceSetup(n)

ipsecCryptoProfileObject = { "name": "MyTestIpsecCryptoProfile", "folder": "Remote Networks", "hash": [ "sha1" ], "dh_group": [ "group5" ], "encryption": [ "aes-128-cbc" ], "lifetime": { "hours": 8 } }
o.paIpsecCryptoProfilesCreate(ipsecCryptoProfileObject)
```

This will create a IPSec Crypto Profile in the "Remote Networks" folder.
```python
o = serviceSetup.serviceSetup(n)

ipsecCryptoProfileObject = { "name": "MyIpsecCryptoProfile", "folder": "Remote Networks", "esp": {"authentication": ["sha512"], "encryption": ["aes-256-cbc"]}, "lifetime": {"hours": 1}, "dh_group": "group20" }
o.paIpsecCryptoProfilesCreate(ipsecCryptoProfileObject, "Remote Networks")
```

## Edit a IPSec Crypto Profile
To edit an existing IPSec Crypto Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = serviceSetup.serviceSetup(n)

ipsecCryptoProfileObject = { "name": "MyIpsecCryptoProfile", "folder": "Remote Networks", "esp": {"authentication": ["sha256"], "encryption": ["aes-256-cbc"]}, "lifetime": {"hours": 1}, "dh_group": "group20" }
o.paIpsecCryptoProfilesEdit(ipsecCryptoProfileObject, "Remote Networks")
```

## Delete a IPSec Crypto Profile
To edit an delete IPSec Crypto Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = serviceSetup.serviceSetup(n)

ipsecCryptoProfileObject = { "name": "MyIpsecCryptoProfile" }
o.paIpsecCryptoProfilesDelete(ipsecCryptoProfileObject, "Remote Networks")
```