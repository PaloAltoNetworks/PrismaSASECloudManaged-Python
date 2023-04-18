# Examples on how to work with Decryption Rules
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

## List all Decryption Rules
To list all Decryption Rules within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paDecryptionRulesList()
```


To list all Decryption Rules within a specific folder, e.g. _Shared_ (it defaults to _Shared_). You can also define the position (It defaults to _pre_).
```python
s = securityServices.securityServices(n)

s.paDecryptionRulesList("Shared", "pre")
```


## Create a Decryption Rule
To create a Decryption Rule in the _Remote Networks_ folder (it defaults to _Shared_). You can also define the position (It defaults to _pre_).

```python
s = securityServices.securityServices(n)

decryptionRule = {"name":"Exempt Healthcare and Financial","folder":"Shared","position":"pre","source_hip":["any"],"action":"no-decrypt","profile":"best-practice","from":["trust"],"to":["untrust"],"source":["any"],"destination":["any"],"source_user":["any"],"category":["financial-services","health-and-medicine"],"service":["any"],"log_setting":"Cortex Data Lake","type":{"ssl_forward_proxy":{}}}
s.paDecryptionRulesCreate(decryptionRule)
```

This will create a Decryption Rule in the "Remote Networks" folder.

```python
s = securityServices.securityServices(n)

decryptionRule = {"name":"Exempt Healthcare and Financial","folder":"Shared","position":"pre","source_hip":["any"],"action":"no-decrypt","profile":"best-practice","from":["trust"],"to":["untrust"],"source":["any"],"destination":["any"],"source_user":["any"],"category":["financial-services","health-and-medicine"],"service":["any"],"log_setting":"Cortex Data Lake","type":{"ssl_forward_proxy":{}}}
s.paDecryptionRulesCreate(decryptionRule, "Remote Networks")
```

## Edit a Decryption Rule
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Decryption Rule in the _Remote Networks_ folder. 

This will edit an existing Decryption Rule named _Sample Policy_.

```python
s = securityServices.securityServices(n)

decryptionRule = {"name":"Exempt Healthcare and Financial","folder":"Shared","position":"pre","source_hip":["any"],"action":"no-decrypt","profile":"best-practice","from":["trust"],"to":["untrust"],"source":["any"],"destination":["any"],"source_user":["any"],"category":["financial-services","health-and-medicine"],"service":["any"],"log_setting":"Cortex Data Lake","type":{"ssl_forward_proxy":{}}}
s.paDecryptionRulesEdit(decryptionRule, "Remote Networks")
```

## Delete a Decryption Rule
To delete a Decryption Rule in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

decryptionRule = { "name": "Exempt Healthcare and Financial" }
s.paDecryptionRulesDelete(decryptionRule, "Remote Networks")
```