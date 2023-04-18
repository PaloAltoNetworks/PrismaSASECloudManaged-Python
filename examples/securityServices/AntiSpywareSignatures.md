# Examples on how to work with Anti-Spyware Signatures
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

## List all Anti-Spyware Signatures
To list all Anti-Spyware Signatures within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paAntiSpywareSignaturesList()
```


To list all Anti-Spyware Signatures within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paAntiSpywareSignaturesList("Shared")
```


## Create a Anti-Spyware Signatures
To create a Anti-Spyware Signatures in the _Shared_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

antiSpywareSignature = {"folder":"Shared","default_action":{"alert":{}},"threatname":"Example Signature","severity":"informational","direction":"both","cve":["CVE-12345"],"signature":{"standard":[{"name":"ExampleSig","scope":"protocol-data-unit","and_condition":[{"name":"And Condition 1","or_condition":[{"name":"Or Condition 1","operator":{"less_than":{"value":0,"context":"ssl-req-client-hello-missing-sni"}}}]}]}]},"threat_id":"15123"}
s.paAntiSpywareSignaturesCreate(antiSpywareSignature)
```

This will create a Anti-Spyware Signature in the "Shared" folder.

```python
s = securityServices.securityServices(n)

antiSpywareSignature = {"folder":"Shared","default_action":{"alert":{}},"threatname":"Example Signature","severity":"informational","direction":"both","cve":["CVE-12345"],"signature":{"standard":[{"name":"ExampleSig","scope":"protocol-data-unit","and_condition":[{"name":"And Condition 1","or_condition":[{"name":"Or Condition 1","operator":{"less_than":{"value":0,"context":"ssl-req-client-hello-missing-sni"}}}]}]}]},"threat_id":"15123"}
s.paAntiSpywareSignaturesCreate(antiSpywareSignature, "Remote Networks")
```

## Edit a Anti-Spyware Signature
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Anti-Spyware Signature in the _Remote Networks_ folder. 

This will edit an existing Anti-Spyware Signature named _Sample Policy_.

```python
s = securityServices.securityServices(n)

antiSpywareSignature = {"folder":"Shared","default_action":{"alert":{}},"threatname":"Example Signature","severity":"informational","direction":"both","cve":["CVE-12345"],"signature":{"standard":[{"name":"EditExampleSig","scope":"protocol-data-unit","and_condition":[{"name":"And Condition 1","or_condition":[{"name":"Or Condition 1","operator":{"less_than":{"value":0,"context":"ssl-req-client-hello-missing-sni"}}}]}]}]},"threat_id":"15123"}
s.paAntiSpywareSignaturesEdit(antiSpywareSignature, "Remote Networks")
```

## Delete a Anti-Spyware Signature
To delete a Anti-Spyware Signature in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

antiSpywareSignature = { "threatname": "Example Signature" }
s.paAntiSpywareSignaturesDelete(antiSpywareSignature, "Remote Networks")
```