# Examples on how to work with Infrastructure Settings
In all examples, it will either return a success or failure when attempting the operation.

## Authentication
First authenticate to the API service:
```python
from auth import saseAuthentication
from access import prismaAccess
from access import serviceSetup

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```

Now we can proceed with the commands below.

## List all Infrastructure Settings
```python
o = serviceSetup.serviceSetup(n)

o.paInfrastructureSettingsListInfrastructureSettings()
```

## Edit Infrastructure Settings
To edit an existing _Infrastructure Setting_. 

Refer to `JSON` output from the List command above to edit appropriately.

```python
o = serviceSetup.serviceSetup(n)

infrastructureSettings = {}

o.paInfrastructureSettingsEditInfrastructureSettings(ServiceConnection1)
```
