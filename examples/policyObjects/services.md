# Examples on how to work with services
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

## List all Services
To list all services within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paServicesListServices()
```


To list all services within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paServicesListServices("Remote Networks")
```


## Create a Service
To create an Service in the _Shared_ folder (it defaults to _Shared_)

```python
o = policyObjects.policyObjects(n)

serviceObject = { "name": "testService", "protocol": { "tcp": { "port": "1234,1239" } } }
o.paServicesCreateService(serviceObject)
```

This will create a service in the "Remote Networks" folder.

```python
o = policyObjects.policyObjects(n)

serviceObject = { "name": "testService", "protocol": { "tcp": { "port": "1234,1239" } } }
o.paServicesCreate(serviceObject, "Remote Networks")
```

## Edit an Services
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing services in the _Remote Networks_ folder. 

This will edit an existing services object named _testService_.

```python
o = policyObjects.policyObjects(n)

serviceObject = { "name": "testService", "protocol": { "tcp": { "port": "30000" } } }
o.paServicesEditService(serviceObject, "Remote Networks")
```

## Delete an Address
To edit an delete address in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

serviceObject = { "name": "testService" }
o.paServicesDeleteService(serviceObject, "Remote Networks")
```