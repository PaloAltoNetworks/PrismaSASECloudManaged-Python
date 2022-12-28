# Examples on how to work with HIP objects
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

## List all HIP Objects
To list all HIP objects within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paHipObjectsListHipObjects()
```


To list all HIP objects within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paHipObjectsListHipObjects("Remote Networks")
```


## Create a HIP Object
To create a HIP Object in the _Shared_ folder (it defaults to _Shared_)
```python
o = policyObjects.policyObjects(n)

hipObject = {"name": "myWindows", "folder": "shared", "host_info": {"criteria": {"os": {"contains": {"Microsoft": "All"}}}}}
o.paHipObjectsCreate(hipObject)
```

This will create a HIP Object in the "Remote Networks" folder.
```python
o = policyObjects.policyObjects(n)

hipObject = {"name": "myWindows", "folder": "shared", "host_info": {"criteria": {"os": {"contains": {"Microsoft": "All"}}}}}
o.paHipObjectsCreate(hipObject, "Remote Networks")
```

## Edit a HIP Object
To edit an existing HIP object in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

hipObject = {"name": "myWindows", "host_info": {"criteria": {"os": {"contains": {"Microsoft": "Windows 10"}}}}, "description": "Matches all Windows 10 endpoints"}
o.paHipObjectsEdit(hipObject, "Remote Networks")
```

## Delete a HIP Object
To edit an delete HIP object in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

hipObject = {"name": "myWindows"}
o.paHipObjectsDelete(hipObject)
```