# Examples on how to work with Profile Groups
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

## List all Profile Groups
To list all Profile Groups within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paProfileGroupsList()
```


To list all Profile Groups within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paProfileGroupsList("Shared")
```


## Create a Profile Group
To create a Profile Group in the _Remote Networks_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

profileGroup = {"name":"best-practice2","folder":"Shared","virus_and_wildfire_analysis":["best-practice2"],"spyware":["best-practice2"],"dns_security":["best-practice2"],"vulnerability":["best-practice2"],"url_filtering":["best-practice2"],"file_blocking":["best-practice2"]}
s.paProfileGroupsCreate(profileGroup)
```

This will create a Profile Group in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

profileGroup = {"name":"best-practice2","folder":"Shared","virus_and_wildfire_analysis":["best-practice2"],"spyware":["best-practice2"],"dns_security":["best-practice2"],"vulnerability":["best-practice2"],"url_filtering":["best-practice2"],"file_blocking":["best-practice2"]}
s.paProfileGroupsCreate(profileGroup, "Remote Networks")
```

## Edit a Profile Group
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Profile Group in the _Remote Networks_ folder. 

This will edit an existing Profile Group named _Sample Policy_.

```python
s = securityServices.securityServices(n)

profileGroup = {"name":"best-practice2","folder":"Shared","virus_and_wildfire_analysis":["best-practice2"],"spyware":["best-practice2"],"dns_security":["best-practice2"],"vulnerability":["best-practice2"],"url_filtering":["best-practice2"],"file_blocking":["best-practice2"]}
s.paProfileGroupsEdit(profileGroup, "Remote Networks")
```

## Delete a Profile Group
To delete a Profile Group in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

profileGroup = { "name": "practice2" }
s.paProfileGroupsDelete(profileGroup, "Remote Networks")
```