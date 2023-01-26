# Examples on how to work with Dynamic User Groups
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

## List all Dynamic User Groups
To list all Dynamic User Groups within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paDynamicUserGroupsListDynamicUserGroups()
```


To list all Dynamic User Groups within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paDynamicUserGroupsListDynamicUserGroups("Remote Networks")
```


## Create a Dynamic User Group
To create a Dynamic User Groups in the _Shared_ folder (it defaults to _Shared_)
```python
o = policyObjects.policyObjects(n)

myDynamicUserGroup = { 'name': 'myDynamicUserGroup2', 'filter': "'ADEM' or 'Microsoft 365' and 'best-practice'" }
o.paDynamicUserGroupsCreate(myDynamicUserGroup)
```

This will create a Dynamic User Groups in the "Remote Networks" folder.
```python
o = policyObjects.policyObjects(n)

myDynamicUserGroup = { 'name': 'myDynamicUserGroup3', 'filter': "'ADEM' or 'Microsoft 365' and 'best-practice'" }
o.paDynamicUserGroupsCreate(myDynamicUserGroup, "Remote Networks")
```

## Edit a Dynamic User Group
To edit an existing Dynamic User Groups in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

myDynamicUserGroup = { 'name': 'myDynamicUserGroup3', 'filter': "'ADEM'" }
o.paDynamicUserGroupsEdit(myDynamicUserGroup, "Remote Networks")
```

## Delete a Dynamic User Group
To delete Dynamic User Group in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

myDynamicUserGroup = { "name": "myDynamicUserGroup3" }
o.paDynamicUserGroupsDelete(myDynamicUserGroup, "Remote Networks")
```