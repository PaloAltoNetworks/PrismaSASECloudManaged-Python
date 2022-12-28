# Examples on how to work with External Dynamic Lists
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

## List all External Dynamic Lists
To list all regions within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paExternalDynamicListsListExternalDynamicLists()
```


To list all External Dynamic Lists within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paExternalDynamicListsListExternalDynamicLists("Remote Networks")
```


## Create a External Dynamic List
To create a External Dynamic List in the _Shared_ folder (it defaults to _Shared_)
```python
o = policyObjects.policyObjects(n)

edlObject = {'name': 'myTestEDL', 'type': {'ip': {'url': 'http://mytestsite.edl/threat-research-ips', 'recurring': {'hourly': {}}, 'description': 'my Test EDL', 'exception_list': ['1.1.1.1'], 'certificate_profile': 'EDL-Hosting-Service-Profile'}}}
o.paExternalDynamicListsCreate(edlObject)
```

This will create a External Dynamic List in the "Remote Networks" folder.
```python
o = policyObjects.policyObjects(n)

edlObject = {'name': 'myTestEDL', 'type': {'ip': {'url': 'http://mytestsite.edl/threat-research-ips', 'recurring': {'hourly': {}}, 'description': 'my Test EDL', 'exception_list': ['1.1.1.1'], 'certificate_profile': 'EDL-Hosting-Service-Profile'}}}
o.paExternalDynamicListsCreate(edlObject, "Remote Networks")
```

## Edit a External Dynamic List
To edit an existing External Dynamic List in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

edlObject = {'name': 'myTestEDL', 'type': {'ip': {'url': 'http://mytestsite.edl/threat-research-ips', 'recurring': {'hourly': {}}, 'description': 'my Test EDL'}}}
o.paExternalDynamicListsEdit(edlObject, "Remote Networks")
```

## Delete a External Dynamic List
To edit an delete External Dynamic List in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

edlObject = {'name': 'myTestEDL'}
o.paExternalDynamicListsDelete(edlObject)
```