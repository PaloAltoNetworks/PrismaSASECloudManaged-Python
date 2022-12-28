# Examples on how to work with service groups
In all examples, it will either return a success or failure when attempting the operation.

## Authentication
First authenticate to the API service:
```python
from auth import saseAuthentication
from access import prismaAccess
from access import policyObjects

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```

Now we can proceed with the commands below.

## List all Service Groups
To list all service groups within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)
o.paServiceGroupsListServiceGroups()
```


To list all service groups within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)
o.paServiceGroupsListServiceGroups("Remote Networks")
```


## Create a Service Group
To create an Service Group in the _Shared_ folder (it defaults to _Shared_)

Assumes the `myCustomService` service is already created.

```python
o = policyObjects.policyObjects(n)

servicesGroupObject = {"name": "myServiceGroup1234", "members": ["service-http", "service-https", "myCustomService"]}
o.paServiceGroupsCreate(servicesGroupObject)
```

This will create a service group in the "Remote Networks" folder.

```python
o = policyObjects.policyObjects(n)

servicesGroupObject = {"name": "myServiceGroup1234", "members": ["service-http", "service-https", "myCustomService"]}
o.paService GroupsCreate(servicesGroupObject, "Remote Networks")
```

## Edit an Service Groups
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing service groups in the _Remote Networks_ folder. 

This will edit an existing service groups object named _testService_.

```python
o = policyObjects.policyObjects(n)

servicesGroupObject = {"name": "myServiceGroup", "members": ["service-https", "myCustomService"]}
o.paServiceGroupsEdit(servicesGroupObject, "Remote Networks")
```

## Delete an Address
To edit an delete address in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

servicesGroupObject = {"name": "myServiceGroup"}
o.paServiceGroupsDelete(servicesGroupObject)
```