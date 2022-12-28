# Examples on how to work with regions
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

## List all Regions
To list all regions within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paRegionsListRegions()
```


To list all regions within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paRegionsListRegions("Remote Networks")
```


## Create a region
To create a region in the _Shared_ folder (it defaults to _Shared_)
```python
o = policyObjects.policyObjects(n)

regionsObject = {"name": "MC", "address": ["1.1.1.0/24"], "geo_location": {"longitude": -178, "latitude": 20}}
o.paRegionsCreate(regionsObject)
```

This will create a region in the "Remote Networks" folder.
```python
o = policyObjects.policyObjects(n)

regionsObject = {"name": "MC", "address": ["1.1.1.0/24"], "geo_location": {"longitude": -178, "latitude": 20}}
o.paRegionsCreate(regionsObject, "Remote Networks")
```

## Edit a region
To edit an existing region in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

regionsObject = {"name": "MC", "address": ["1.1.2.0/24"], "geo_location": {"longitude": -160, "latitude": 30}}
o.paRegionsEdit(regionsObject, "Remote Networks")
```

## Delete a region
To edit an delete region in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

regionsObject = {"name": "MC"}
o.paRegionsDelete(regionsObject)
```