# Examples on how to work with Http Header Profiles
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

## List all Http Header Profiles
To list all Http Header Profiles within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paHttpHeaderProfilesList()
```


To list all Http Header Profiles within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paHttpHeaderProfilesList("Shared")
```


## Create a Http Header Profile
To create a Http Header Profile in the _Remote Networks_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

httpHeaderProfiles = {"name":"ExampleProfile","folder":"Shared","http_header_insertion":[{"name":"Example","type":[{"name":"Dropbox Network Control","headers":[{"name":"example123","header":"X-Dropbox-allowed-Team-Ids","value":"test123","log":True}],"domains":["*.dropbox.com"]}]}]}
s.paHttpHeaderProfilesCreate(httpHeaderProfiles)
```

This will create a Http Header Profile in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

httpHeaderProfiles = {"name":"ExampleProfile","folder":"Shared","http_header_insertion":[{"name":"Example","type":[{"name":"Dropbox Network Control","headers":[{"name":"example123","header":"X-Dropbox-allowed-Team-Ids","value":"test123","log":True}],"domains":["*.dropbox.com"]}]}]}
s.paHttpHeaderProfilesCreate(httpHeaderProfiles, "Remote Networks")
```

## Edit a Http Header Profile
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Http Header Profile in the _Remote Networks_ folder. 

This will edit an existing Http Header Profile named _Sample Policy_.

```python
s = securityServices.securityServices(n)

httpHeaderProfiles = {"name":"ExampleProfile","folder":"Shared","http_header_insertion":[{"name":"Example","type":[{"name":"Dropbox Network Control","headers":[{"name":"example123","header":"X-Dropbox-allowed-Team-Ids","value":"test123","log":True}],"domains":["*.dropbox.com"]}]}]}
s.paHttpHeaderProfilesEdit(httpHeaderProfiles, "Remote Networks")
```

## Delete a Http Header Profile
To delete a Http Header Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

httpHeaderProfiles = { "name": "ExampleProfile" }
s.paHttpHeaderProfilesDelete(httpHeaderProfiles, "Remote Networks")
```