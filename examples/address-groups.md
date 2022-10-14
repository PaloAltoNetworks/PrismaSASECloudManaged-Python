# Examples on how to work with address groups
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

## List all Address Groups
To list all addresses within shared folder (it defaults to _Shared_ folder)
```python
n.paAddressGroupsListAddressGroups()
```


To list all addresses within a specific folder, e.g. _Remote Networks_
```python
n.paAddressGroupsListAddressGroups("Remote Networks")
```


## Create an address-group
To create an address-group in the _Shared_ folder (it defaults to _Shared_)

Assumes that the `MyTag` tag is created, as well as address objects `testObject2` and `testObject4`.
```python
exampleGroupObject = { "name": "testGroupObject1234", "description": "Test group object description", "tag": ["MyTag"], "static": ["testObject2", "testObject4"]}
n.paAddressGroupsCreate(exampleGroupObject)

```

This will create an address in the "Remote Networks" folder.

Assumes that the `MyTag` tag is created, as well as address objects `testObject2` and `testObject4`.
```python
exampleGroupObject = { "name": "testGroupObject1234", "description": "Test group object description", "tag": ["MyTag"], "static": ["testObject2", "testObject4"]}
n.paAddressGroupsCreate(exampleGroupObject, "Remote Networks")
```

## Edit an Address
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing address in the _Remote Networks_ folder. 

This will edit an existing address object named _testGroupObject1234_.
Assumes that `testObject2` and `testObject4` both exist.

```python
exampleGroupObject = { "name": "testGroupObject1234", "description": "Test group123 object description", "static": ["testObject2", "testObject4"]}
n.paAddressGroupsEdit(exampleGroupObject, "Remote Networks")
```

## Delete an Address
To edit an delete address in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
exampleGroupObject = { "name": "testGroupObject1234" }
n.paAddressesDelete(exampleGroupObject, "Remote Networks")
```