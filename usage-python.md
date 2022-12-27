# Python usage
There are 2 methods to authenticate, either by creating an _authToken.json_ file with the following format (these values are fake):
```json
{
    "tsg_id": "1234567890",
    "client_id": "pan.svc.acct.access@1234567890.iam.randomaccount.com",
    "client_secret": "1234afbe-beac-12d6-aa95-13425671a919c"
}
```

Now we start with the python code:
```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
```


Alternatively, you can submit the information as part of the initialization within Python:
```python
from auth import saseAuthentication
from access import prismaAccess
from access import policyObjects

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuth("1234567890","pan.svc.acct.access@1234567890.iam.randomaccount.com","1234afbe-beac-12d6-aa95-13425671a919c")
n = prismaAccess.prismaAccess(p.saseToken)
```

In both cases, if it works, no errors will be displayed.


Now that we have the Auth Token created, we can run commands on the Prisma Access Cloud Managed environment:
```python
o = policyObjects.policyObjects(n)

o.paTagsListTags()
```

Resulting output will look like the following:
```json
{"data": [{"name": "Sanctioned", "folder": "predefined", "color": "Olive"}, {"name": "empty", "folder": "predefined"}, {"id": "3af5d3bd-68e6-4ab1-8a66-578f757983a1", "name": "best-practice", "folder": "Shared", "color": "Green"}, {"id": "06f69745-df4f-4b03-b39f-9853fa43928b", "name": "Microsoft 365", "folder": "Shared", "color": "Red"}, {"id": "d5385310-3993-4c83-86ac-e592290d9109", "name": "ADEM", "folder": "Shared", "color": "Blue", "comments": "test"}], "offset": 0, "total": 5, "limit": 200}
```

# Detailed examples
## Policy Objects
* [tags](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/policyObjects/tags.md)
* [address objects](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/policyObjects/addresses.md)
* [address group objects](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/policyObjects/address-groups.md)
* [services](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/policyObjects/services.md)
* [application filters](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/policyObjects/application-filters.md)
* [application groups](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/policyObjects/application-groups.md)


## Service Setup
* [IKE Crypto Profiles](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/serviceSetup/ike-crypto-profiles.md)
* [IKE Gateways](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/serviceSetup/ike-gateways.md)
* [IPSec Crypto Profiles](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/serviceSetup/ipsec-crypto-profiles.md)
* [IPSec Tunnels](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/serviceSetup/ipsec-tunnels.md)
* [Service Connections](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/serviceSetup/service-connections.md)
* [Remote Networks](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/serviceSetup/remote-networks.md)
* [Infrastructure Settings](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/serviceSetup/shared-infrastructure-settings.md)