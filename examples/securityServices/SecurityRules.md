# Examples on how to work with Security Rules
In all examples, it will either return a success or failure when attempting the operation.

## Authentication
First authenticate to the API service:
```python
from auth import saseAuthentication
from access import prismaAccess
from access import securityServices

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```

Now we can proceed with the commands below.

## List all Security Rules
To list all security rules within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paSecurityRulesList()
```


To list all security rules within a specific folder, e.g. _Shared_ (it defaults to _Shared_). You can also define the position (It defaults to _pre_).
```python
s = securityServices.securityServices(n)

s.paSecurityRulesList("Shared", "pre")
```


## Create a Security Rule
To create a security rule in the _Remote Networks_ folder (it defaults to _Shared_). You can also define the position (It defaults to _pre_).

```python
s = securityServices.securityServices(n)

securityRule = {"name":"Sample Policy","folder":"Shared","position":"pre","action":"allow","application":["ping"],"category":["any"],"description":"Description of Sample Policy","destination":["any"],"destination_hip":["any"],"disabled":False,"from":["trust"],"log_setting":"Cortex Data Lake","negate_destination":False,"negate_source":False,"profile_setting":{"group":["best-practice"]},"service":["any"],"source":["any"],"source_hip":["any"],"source_user":["any"],"tag":[],"to":["untrust"]}
s.paSecurityRulesCreate(securityRule)
```

This will create a security rule in the "Shared" folder.

```python
s = securityServices.securityServices(n)

securityRule = {"name":"Sample Policy","folder":"Shared","position":"pre","action":"allow","application":["ping"],"category":["any"],"description":"Description of Sample Policy","destination":["any"],"destination_hip":["any"],"disabled":False,"from":["trust"],"log_setting":"Cortex Data Lake","negate_destination":False,"negate_source":False,"profile_setting":{"group":["best-practice"]},"service":["any"],"source":["any"],"source_hip":["any"],"source_user":["any"],"tag":[],"to":["untrust"]}
s.paSecurityRulesCreate(securityRule, "Remote Networks")
```

## Edit a Security Rule
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing security rule in the _Remote Networks_ folder. 

This will edit an existing security rule named _Sample Policy_.

```python
s = securityServices.securityServices(n)

securityRule = {"name":"Sample Policy","folder":"Shared","position":"pre","action":"allow","application":["ping"],"category":["any"],"description":"Edited Description of Sample Policy","destination":["any"],"destination_hip":["any"],"disabled":False,"from":["trust"],"log_setting":"Cortex Data Lake","negate_destination":False,"negate_source":False,"profile_setting":{"group":["best-practice"]},"service":["any"],"source":["any"],"source_hip":["any"],"source_user":["any"],"tag":[],"to":["untrust"]}
s.paSecurityRulesEdit(securityRule, "Remote Networks")
```

## Delete a Security Rule
To delete a security rule in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

securityRule = { "name": "Sample Policy" }
s.paSecurityRulesDelete(securityRule, "Remote Networks")
```