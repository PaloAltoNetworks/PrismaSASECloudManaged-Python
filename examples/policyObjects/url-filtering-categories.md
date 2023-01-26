# Examples on how to work with URL Filtering Categories
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

## List all URL Filtering Categories
To list all URL Filtering Categories within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paUrlFilteringCategoriesListUrlFilteringCategories()
```