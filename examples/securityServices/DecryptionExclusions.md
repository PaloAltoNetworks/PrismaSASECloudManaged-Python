# Examples on how to work with Decryption Exclusions
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

## List all Decryption Exclusions
To list all Decryption Exclusions within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paDecryptionExclusionsList()
```


To list all Decryption Exclusions within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paDecryptionExclusionsList("Shared")
```


## Create a Decryption Exclusion
To create a Decryption Exclusion in the _Remote Networks_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

decryptionExclusions = {"name":"https://*.example.com","description":"Example exclusion"}
s.paDecryptionExclusionsCreate(decryptionExclusions)
```

This will create a Decryption Exclusion in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

decryptionExclusions = {"name":"https://*.example.com","description":"Example exclusion"}
s.paDecryptionExclusionsCreate(decryptionExclusions, "Remote Networks")
```

## Edit a Decryption Exclusion
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Decryption Exclusion in the _Remote Networks_ folder. 

This will edit an existing Decryption Exclusion named _Sample Policy_.

```python
s = securityServices.securityServices(n)

decryptionExclusions = {"name":"https://*.example.com","description":"Example exclusion"}
s.paDecryptionExclusionsEdit(decryptionExclusions, "Remote Networks")
```

## Delete a Decryption Exclusion
To delete a Decryption Exclusion in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

decryptionExclusions = { "name": "https://*.example.com" }
s.paDecryptionExclusionsDelete(decryptionExclusions, "Remote Networks")
```