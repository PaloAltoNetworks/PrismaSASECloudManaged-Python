# Examples on how to work with HIP Profiles
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

## List all HIP Profiles
To list all HIP profiles within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paHipObjectsListHipObjects()
```


To list all HIP profiles within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paHipObjectsListHipObjects("Remote Networks")
```


## Create a HIP Profile
To create a HIP Profile in the _Shared_ folder (it defaults to _Shared_)
_Take note that because the `match` criteria needs double quotes around it, we use single quotes for the dict_

```python
o = policyObjects.policyObjects(n)

hipProfileObject = {'name': 'myCorporateAsset', 'match': '"is-win"  and "is-anti-malware-installed-1day"  and "is-firewall-enabled"  and "is-patch-management-enabled"  and "is-disk-backup-installed-1day"  and "is-disk-encryption-installed" ', 'description': 'My Corporate Asset'}
o.paHipProfilesCreate(hipProfileObject)
```

This will create a HIP Profile in the "Remote Networks" folder.
_Take note that because the `match` criteria needs double quotes around it, we use single quotes for the dict_

```python
o = policyObjects.policyObjects(n)

hipProfileObject = {'name': 'myCorporateAsset', 'match': '"is-win"  and "is-anti-malware-installed-1day"  and "is-firewall-enabled"  and "is-patch-management-enabled"  and "is-disk-backup-installed-1day"  and "is-disk-encryption-installed" ', 'description': 'My Corporate Asset'}
o.paHipProfilesCreate(hipProfileObject, "Remote Networks")

```

## Edit a HIP Profiles
To edit an existing HIP Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument
_Take note that because the `match` criteria needs double quotes around it, we use single quotes for the dict_

```python
o = policyObjects.policyObjects(n)

hipProfileObject = {'name': 'myCorporateAsset', 'match': '"is-win"  and "is-firewall-enabled"  and "is-patch-management-enabled"  and "is-disk-backup-installed-1day"  and "is-disk-encryption-installed" ', 'description': 'My Corporate Asset - Adjusted'}
o.paHipProfilesEdit(hipProfileObject, "Remote Networks")
```

## Delete a HIP Profile
To edit an delete HIP profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

hipProfileObject = {'name': 'myCorporateAsset'}
o.paHipProfilesDelete(hipProfileObject, "Remote Networks")
```