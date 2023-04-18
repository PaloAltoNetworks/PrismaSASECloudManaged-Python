# Examples on how to work with Wildfire AntiVirus Profiles
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

## List all Wildfire AntiVirus Profiles
To list all Wildfire AntiVirus Profiles within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paWildfireAntiVirusProfilesList()
```


To list all Wildfire AntiVirus Profiles within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paWildfireAntiVirusProfilesList("Shared")
```


## Create a Wildfire AntiVirus Profile
To create a Wildfire AntiVirus Profile in the _Remote Networks_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

wildfireAntiVirusProfiles = {"name":"best-practice2","folder":"Shared","rules":[{"name":"default","application":["any"],"file_type":["any"],"direction":"both","analysis":"public-cloud"}],"description":"Best practice antivirus and wildfire analysis security profile"}
s.paWildfireAntiVirusProfilesCreate(wildfireAntiVirusProfiles)
```

This will create a Wildfire AntiVirus Profile in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

wildfireAntiVirusProfiles = {"name":"best-practice2","folder":"Shared","rules":[{"name":"default","application":["any"],"file_type":["any"],"direction":"both","analysis":"public-cloud"}],"description":"Best practice antivirus and wildfire analysis security profile"}
s.paWildfireAntiVirusProfilesCreate(wildfireAntiVirusProfiles, "Remote Networks")
```

## Edit a Wildfire AntiVirus Profile
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Wildfire AntiVirus Profile in the _Remote Networks_ folder. 

This will edit an existing Wildfire AntiVirus Profile named _Sample Policy_.

```python
s = securityServices.securityServices(n)

wildfireAntiVirusProfiles = {"name":"best-practice2","folder":"Shared","rules":[{"name":"default","application":["any"],"file_type":["any"],"direction":"both","analysis":"public-cloud"}],"description":"Best practice antivirus and wildfire analysis security profile"}
s.paWildfireAntiVirusProfilesEdit(wildfireAntiVirusProfiles, "Remote Networks")
```

## Delete a Wildfire AntiVirus Profile
To delete a Wildfire AntiVirus Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

wildfireAntiVirusProfiles = { "name": "best-practice2" }
s.paWildfireAntiVirusProfilesDelete(wildfireAntiVirusProfiles, "Remote Networks")
```