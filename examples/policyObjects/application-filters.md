# Examples on how to work with application filters
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

## List all Application Filters
To list all application filters within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paApplicationFiltersListApplicationFilters()
```


To list all application filters within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paApplicationFiltersListApplicationFilters("Remote Networks")
```


## Create an Application Filter
To create an application filter in the _Shared_ folder (it defaults to _Shared_)

```python
o = policyObjects.policyObjects(n)

applicationFilterObject = { "name": "myTestApplicationFilter2", "subcategory": ["audio-streaming"], "technology": ["browser-based"], "risk": [4], "pervasive": True }
o.paApplicationFiltersCreate(applicationFilterObject)
```

This will create an application filter in the "Remote Networks" folder.

```python
o = policyObjects.policyObjects(n)

applicationFilterObject = { "name": "myTestApplicationFilter2", "subcategory": ["audio-streaming"], "technology": ["browser-based"], "risk": [4], "pervasive": True }
o.paApplicationFiltersCreate(applicationFilterObject, "Remote Networks")
```

## Edit an Application Filter
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing application filter in the _Remote Networks_ folder. 

This will edit an existing application filter object named _myTestApplicationFilter2_.

```python
o = policyObjects.policyObjects(n)

applicationFilterObject = { "name": "myTestApplicationFilter2", "subcategory": ["audio-streaming"], "technology": ["client-server"], "risk": [4], "pervasive": True }
o.paApplicationFiltersEdit(applicationFilterObject, "Remote Networks")
```

## Delete an Application Filter
To delete an Application Filter in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

applicationFilterObject = { "name": "myTestApplicationFilter2" }
o.paApplicationFiltersDelete(applicationFilterObject, "Remote Networks")
```