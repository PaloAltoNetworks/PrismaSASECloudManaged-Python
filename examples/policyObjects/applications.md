# Examples on how to work with applications
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

## List all Applications
To list all applications within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paApplicationsListApplications()
```


To list all applications within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paApplicationsListApplications("Remote Networks")
```


## Create an Applications
To create an application in the _Shared_ folder (it defaults to _Shared_)

```python
o = policyObjects.policyObjects(n)

applicationFilterObject = { "name": "myTestApplicationFilter2", "subcategory": ["audio-streaming"], "technology": ["browser-based"], "risk": [4], "pervasive": True }
o.paApplicationFiltersCreate(applicationFilterObject)
```

This will create an application filter in the "Remote Networks" folder.

```python
o = policyObjects.policyObjects(n)

applicationsObject = { "name": "myTestApp12345", "category": "media", "subcategory": "audio-streaming", "technology": "client-server", "default": { "port": [ "tcp/80", "tcp/443" ] }, "risk": 1}
o.paApplicationsCreate(applicationsObject)
```

## Edit an Application Filter
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing application filter in the _Remote Networks_ folder. 

This will edit an existing application filter object named _myTestApplicationFilter2_.

```python
o = policyObjects.policyObjects(n)

applicationsObject = { "name": "myTestApp12345", "category": "media", "subcategory": "audio-streaming", "technology": "client-server", "default": { "port": [ "tcp/81", "tcp/4441" ] }, "risk": 4}
o.paApplicationsEdit(applicationsObject, "Remote Networks")
```

## Delete an Application Filter
To delete an Application Filter in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

applicationsObject = { "name": "myTestApp12345" }
o.paApplicationsDelete(applicationsObject)
```