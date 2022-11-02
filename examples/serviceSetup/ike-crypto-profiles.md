# Examples on how to work with IKE Crypto Profiles
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

## List all IKE Crypto Profiles
To list all IKE Crypto Profiles within shared folder (it defaults to _Shared_ folder)
```python
n.paIkeCryptoProfilesListIkeCryptoProfiles()
```


To list all IKE Crypto Profiles within a specific folder, e.g. _Remote Networks_
```python
n.paIkeCryptoProfilesListIkeCryptoProfiles("Remote Networks")
```


## Create an IKE Crypto Profile
To create an IKE Crypto Profile in the _Shared_ folder (it defaults to _Shared_)
```python
ikeCryptoProfileObject = { "name": "MyTestIkeCryptoProfile", "folder": "Remote Networks", "hash": [ "sha1" ], "dh_group": [ "group5" ], "encryption": [ "aes-128-cbc" ], "lifetime": { "hours": 8 } }
n.paIkeCryptoProfilesCreate(ikeCryptoProfileObject)
```

This will create a IKE Crypto Profile in the "Remote Networks" folder.
```python
ikeCryptoProfileObject = { "name": "MyTestIkeCryptoProfile", "folder": "Remote Networks", "hash": [ "sha1" ], "dh_group": [ "group5" ], "encryption": [ "aes-128-cbc" ], "lifetime": { "hours": 8 } }
n.paIkeCryptoProfilesCreate(ikeCryptoProfileObject, "Remote Networks")
```

## Edit a IKE Crypto Profile
To edit an existing IKE Crypto Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
ikeCryptoProfileObject = { "name": "MyTestIkeCryptoProfile", "folder": "Remote Networks", "hash": [ "sha256" ], "dh_group": [ "group5" ], "encryption": [ "aes-128-cbc" ], "lifetime": { "hours": 8 } }
n.paIkeCryptoProfilesEdit(ikeCryptoProfileObject, "Remote Networks")
```

## Delete a IKE Crypto Profile
To edit an delete IKE Crypto Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
ikeCryptoProfileObject = { "name": "MyTestIkeCryptoProfile" }
n.paIkeCryptoProfilesDelete(ikeCryptoProfileObject, "Remote Networks")
```