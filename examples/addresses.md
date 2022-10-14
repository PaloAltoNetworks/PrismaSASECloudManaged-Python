# Examples on how to work with addresses
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

## List all Addresses
To list all addresses within shared folder (it defaults to _Shared_ folder)
```python
n.paAddressesListAddresses()
```


To list all addresses within a specific folder, e.g. _Remote Networks_
```python
n.paAddressesListAddresses("Remote Networks")
```


## Create an address
To create an address in the _Shared_ folder (it defaults to _Shared_)

Assumes that the `ADEM` tag is created
```python
addressObject = { "name": "testObject2", "fqdn": "thisisahostname.com", "tag": [ "ADEM" ] }
n.paAddressesCreate(addressObject)
```

This will create an address in the "Remote Networks" folder.

Assumes that the `ADEM` tag is created
```python
addressObject = { "name": "testObject2", "fqdn": "thisisahostname.com", "tag": [ "ADEM" ] }
n.paAddressesCreate(addressObject, "Remote Networks")
```

## Edit an Address
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing address in the _Remote Networks_ folder. 

This will edit an existing address object named _testObject2_.
Assumes that the `ADEM` tag is created

```python
addressObject = { "name": "testObject2", "ip_netmask": "1.1.1.1", "tag": [ "ADEM" ] }
n.paAddressesEdit(addressObject, "Remote Networks")
```

## Delete an Address
To edit an delete address in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
addressObject = { "name": "testObject2" }
n.paAddressesDelete(addressObject, "Remote Networks")
```