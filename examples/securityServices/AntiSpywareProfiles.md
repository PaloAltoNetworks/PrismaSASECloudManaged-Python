# Examples on how to work with Anti-Spyware Profiles
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

## List all Anti-Spyware Profiles
To list all Anti-Spyware Profiles within shared folder (it defaults to _Shared_ folder)
```python
s = securityServices.securityServices(n)

s.paAntiSpywareProfilesList()
```


To list all Anti-Spyware Profiles within a specific folder, e.g. _Shared_ (it defaults to _Shared_).
```python
s = securityServices.securityServices(n)

s.paAntiSpywareProfilesList("Shared")
```


## Create an Anti-Spyware Profile
To create an Anti-Spyware Profile in the _Shared_ folder (it defaults to _Shared_).

```python
s = securityServices.securityServices(n)

antiSpywareProfile = {"name":"best-practice2","folder":"Shared","description":"Best practice anti-spyware security profile","cloud_inline_analysis":True,"mica_engine_spyware_enabled":[{"name":"HTTP Command and Control detector","inline_policy_action":"reset-both"},{"name":"HTTP2 Command and Control detector","inline_policy_action":"reset-both"},{"name":"SSL Command and Control detector","inline_policy_action":"reset-both"},{"name":"Unknown-TCP Command and Control detector","inline_policy_action":"reset-both"},{"name":"Unknown-UDP Command and Control detector","inline_policy_action":"reset-both"}],"rules":[{"name":"simple-critical","action":{"reset_both":{}},"severity":["critical"],"category":"any","packet_capture":"single-packet"},{"name":"simple-high","action":{"reset_both":{}},"severity":["high"],"category":"any","packet_capture":"single-packet"},{"name":"simple-medium","action":{"reset_both":{}},"severity":["medium"],"category":"any","packet_capture":"single-packet"},{"name":"simple-informational","severity":["informational"],"category":"any","packet_capture":"single-packet"},{"name":"simple-low","severity":["low"],"category":"any","packet_capture":"single-packet"}]}
s.paAntiSpywareProfilesCreate(antiSpywareProfile)
```

This will create a Anti-Spyware Profile in the "Remote Networks" folder.

```python
s = securityServices.securityServices(n)

antiSpywareProfile = {"name":"best-practice2","folder":"Shared","description":"Best practice anti-spyware security profile","cloud_inline_analysis":True,"mica_engine_spyware_enabled":[{"name":"HTTP Command and Control detector","inline_policy_action":"reset-both"},{"name":"HTTP2 Command and Control detector","inline_policy_action":"reset-both"},{"name":"SSL Command and Control detector","inline_policy_action":"reset-both"},{"name":"Unknown-TCP Command and Control detector","inline_policy_action":"reset-both"},{"name":"Unknown-UDP Command and Control detector","inline_policy_action":"reset-both"}],"rules":[{"name":"simple-critical","action":{"reset_both":{}},"severity":["critical"],"category":"any","packet_capture":"single-packet"},{"name":"simple-high","action":{"reset_both":{}},"severity":["high"],"category":"any","packet_capture":"single-packet"},{"name":"simple-medium","action":{"reset_both":{}},"severity":["medium"],"category":"any","packet_capture":"single-packet"},{"name":"simple-informational","severity":["informational"],"category":"any","packet_capture":"single-packet"},{"name":"simple-low","severity":["low"],"category":"any","packet_capture":"single-packet"}]}
s.paAntiSpywareProfilesCreate(antiSpywareProfile, "Remote Networks")
```

## Edit an Anti-Spyware Profile
It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

To edit an existing Anti-Spyware Profile in the _Remote Networks_ folder. 

This will edit an existing Anti-Spyware Profile named _Sample Policy_.

```python
s = securityServices.securityServices(n)

antiSpywareProfile = {"name":"best-practice2","folder":"Shared","description":"Edit Best practice anti-spyware security profile","cloud_inline_analysis":True,"mica_engine_spyware_enabled":[{"name":"HTTP Command and Control detector","inline_policy_action":"reset-both"},{"name":"HTTP2 Command and Control detector","inline_policy_action":"reset-both"},{"name":"SSL Command and Control detector","inline_policy_action":"reset-both"},{"name":"Unknown-TCP Command and Control detector","inline_policy_action":"reset-both"},{"name":"Unknown-UDP Command and Control detector","inline_policy_action":"reset-both"}],"rules":[{"name":"simple-critical","action":{"reset_both":{}},"severity":["critical"],"category":"any","packet_capture":"single-packet"},{"name":"simple-high","action":{"reset_both":{}},"severity":["high"],"category":"any","packet_capture":"single-packet"},{"name":"simple-medium","action":{"reset_both":{}},"severity":["medium"],"category":"any","packet_capture":"single-packet"},{"name":"simple-informational","severity":["informational"],"category":"any","packet_capture":"single-packet"},{"name":"simple-low","severity":["low"],"category":"any","packet_capture":"single-packet"}]}
s.paAntiSpywareProfilesEdit(antiSpywareProfile, "Remote Networks")
```

## Delete an Anti-Spyware Profile
To delete an Anti-Spyware Profile in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
s = securityServices.securityServices(n)

antiSpywareProfile = {"name":"best-practice2"}
s.paAntiSpywareProfilesDelete(antiSpywareProfile, "Remote Networks")
```