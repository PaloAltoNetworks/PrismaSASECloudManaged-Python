# Examples on how to work with Application Groups
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

## List all Application Groups
To list all application groups within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paApplicationGroupsListGroups()
```


To list all application groups within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paApplicationGroupsListGroups("Remote Networks")
```


## Create an Application Groups
To create an application group in the _Shared_ folder (it defaults to _Shared_)

```python
o = policyObjects.policyObjects(n)

applicationGroupObject = {"name": "myTestApplicationGroup", "members": ["web-browsing", "ssl", "Microsoft 365 Access", "myTestApplicationFilter"]}
o.paApplicationGroupsCreate(applicationGroupObject)
```

This will create an application filter in the "Remote Networks" folder.

```python
o = policyObjects.policyObjects(n)

applicationGroupObject = {"name": "myTestApplicationGroup", "members": ["web-browsing", "ssl", "Microsoft 365 Access", "myTestApplicationFilter"]}
o.paApplicationGroupsCreate(applicationGroupObject, "Remote Networks")
```

## Edit an Application Groups
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing application group in the _Remote Networks_ folder. 

This will edit an existing application filter object named _myTestApplicationGroup_.

```python
o = policyObjects.policyObjects(n)

applicationGroupObject = {"name": "myTestApplicationGroup", "members": ["web-browsing", "Microsoft 365 Access", "myTestApplicationFilter"]}
o.paApplicationFiltersEdit(applicationFilterObject, "Remote Networks")
```

## Delete an Application Groups
To delete an Application Groups in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

applicationGroupObject = { "name": "myTestApplicationGroup" }
o.paApplicationGroupsDelete(applicationGroupObject)
```