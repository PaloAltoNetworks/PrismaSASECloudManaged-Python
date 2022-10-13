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

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuth("1234567890","pan.svc.acct.access@1234567890.iam.randomaccount.com","1234afbe-beac-12d6-aa95-13425671a919c")
n = prismaAccess.prismaAccess(p.saseToken)
```

In both cases, if it works, no errors will be displayed.


Now that we have the Auth Token created, we can run commands on the Prisma Access Cloud Managed environment:
```python
n.paTagsListTags()
```

Resulting output will look like the following:
```csv
Tag Folder,Tag Name,Tag Color,Tag Comments
predefined,Sanctioned,Olive,
predefined,empty,,
Shared,best-practice,Green,
Shared,Microsoft 365,Red,
Shared,ADEM,Blue,test
Shared,ExampleTag,Yellow,test tag object.
```

# Detailed examples
## Policy Objects
* [tags](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/tags.md)
* [address objects](https://github.com/PaloAltoNetworks/PrismaSASECloudManaged-Python/blob/main/examples/addresses.md)