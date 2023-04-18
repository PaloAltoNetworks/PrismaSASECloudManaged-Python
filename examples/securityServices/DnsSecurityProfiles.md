# Examples on how to work with Dns Security Profiles
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

## List all Decryption Profiles
To list all Decryption Profiles within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paDnsSecurityProfilesList()
```


To list all Decryption Profiles within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paDecryptionProfilesList("Shared")
```


## Create a Decryption Profile
To create a Decryption Profile in the _Remote Networks_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

dnsSecurityProfiles = {"name":"best-practice2","folder":"Shared","botnet_domains":{"dns_security_categories":[{"name":"pan-dns-sec-grayware","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-recent","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-parked","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-proxy","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-cc","log_level":"default","action":"sinkhole","packet_capture":"single-packet"},{"name":"pan-dns-sec-ddns","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-phishing","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-malware","log_level":"default","action":"sinkhole","packet_capture":"disable"}],"lists":[{"name":"default-paloalto-dns","packet_capture":"disable","action":{"sinkhole":{}}}],"sinkhole":{"ipv4_address":"pan-sinkhole-default-ip","ipv6_address":"::1"}},"description":"Best practice dns security profile"}
s.paDecryptionProfilesCreate(decryptionProfiles)
```

This will create a Decryption Profile in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

decryptionProfiles = {"name":"best-practice2","folder":"Shared","botnet_domains":{"dns_security_categories":[{"name":"pan-dns-sec-grayware","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-recent","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-parked","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-proxy","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-cc","log_level":"default","action":"sinkhole","packet_capture":"single-packet"},{"name":"pan-dns-sec-ddns","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-phishing","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-malware","log_level":"default","action":"sinkhole","packet_capture":"disable"}],"lists":[{"name":"default-paloalto-dns","packet_capture":"disable","action":{"sinkhole":{}}}],"sinkhole":{"ipv4_address":"pan-sinkhole-default-ip","ipv6_address":"::1"}},"description":"Best practice dns security profile"}
s.paDecryptionProfilesCreate(decryptionProfiles, "Remote Networks")
```

## Edit a Decryption Profile
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Decryption Profile in the _Remote Networks_ folder. 

This will edit an existing Decryption Profile named _Sample Policy_.

```python
s = securityServices.securityServices(n)

decryptionProfiles = {"name":"best-practice2","folder":"Shared","botnet_domains":{"dns_security_categories":[{"name":"pan-dns-sec-grayware","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-recent","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-parked","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-proxy","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-cc","log_level":"default","action":"sinkhole","packet_capture":"single-packet"},{"name":"pan-dns-sec-ddns","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-phishing","log_level":"default","action":"sinkhole","packet_capture":"disable"},{"name":"pan-dns-sec-malware","log_level":"default","action":"sinkhole","packet_capture":"disable"}],"lists":[{"name":"default-paloalto-dns","packet_capture":"disable","action":{"sinkhole":{}}}],"sinkhole":{"ipv4_address":"pan-sinkhole-default-ip","ipv6_address":"::1"}},"description":"Best practice dns security profile"}
s.paDecryptionProfilesEdit(decryptionProfiles, "Remote Networks")
```

## Delete a Decryption Profile
To delete a Decryption Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

decryptionProfiles = { "name": "best-practice2" }
s.paDecryptionProfilesDelete(decryptionProfiles, "Remote Networks")
```