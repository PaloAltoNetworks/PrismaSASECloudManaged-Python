# Examples on how to work with Decryption Profiles
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

s.paDecryptionProfilesList()
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

decryptionProfiles = { "name": "best-practice2", "folder": "All", "snippet": "predefined-snippet", "ssl_no_proxy": { "block_expired_certificate": True, "block_untrusted_issuer": True }, "ssl_forward_proxy": { "block_expired_certificate": True, "block_untrusted_issuer": True, "block_unknown_cert": True, "restrict_cert_exts": True, "auto_include_altname": True, "block_unsupported_version": True, "block_unsupported_cipher": True, "block_client_cert": True }, "ssl_inbound_proxy": { "block_unsupported_version": True, "block_unsupported_cipher": True }, "ssl_protocol_settings": { "min_version": "tls1-2", "enc_algo_3des": False, "enc_algo_rc4": False, "auth_algo_sha1": False } }
s.paDecryptionProfilesCreate(decryptionProfiles)
```

This will create a Decryption Profile in the _"Remote Networks"_ folder.

```python
s = securityServices.securityServices(n)

decryptionProfiles = { "name": "best-practice2", "folder": "All", "snippet": "predefined-snippet", "ssl_no_proxy": { "block_expired_certificate": True, "block_untrusted_issuer": True }, "ssl_forward_proxy": { "block_expired_certificate": True, "block_untrusted_issuer": True, "block_unknown_cert": True, "restrict_cert_exts": True, "auto_include_altname": True, "block_unsupported_version": True, "block_unsupported_cipher": True, "block_client_cert": True }, "ssl_inbound_proxy": { "block_unsupported_version": True, "block_unsupported_cipher": True }, "ssl_protocol_settings": { "min_version": "tls1-2", "enc_algo_3des": False, "enc_algo_rc4": False, "auth_algo_sha1": False } }
s.paDecryptionProfilesCreate(decryptionProfiles, "Remote Networks")
```

## Edit a Decryption Profile
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Decryption Profile in the _Remote Networks_ folder. 

This will edit an existing Decryption Profile named _Sample Policy_.

```python
s = securityServices.securityServices(n)

decryptionProfiles = { "name": "best-practice2", "folder": "All", "snippet": "predefined-snippet", "ssl_no_proxy": { "block_expired_certificate": True, "block_untrusted_issuer": True }, "ssl_forward_proxy": { "block_expired_certificate": True, "block_untrusted_issuer": True, "block_unknown_cert": True, "restrict_cert_exts": True, "auto_include_altname": True, "block_unsupported_version": True, "block_unsupported_cipher": True, "block_client_cert": True }, "ssl_inbound_proxy": { "block_unsupported_version": True, "block_unsupported_cipher": True }, "ssl_protocol_settings": { "min_version": "tls1-2", "enc_algo_3des": False, "enc_algo_rc4": False, "auth_algo_sha1": False } }
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