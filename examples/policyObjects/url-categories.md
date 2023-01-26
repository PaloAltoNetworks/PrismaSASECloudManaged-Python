# Examples on how to work with URL Categories
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

## List all URL Categories
To list all URL Categories within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paUrlCategoriesListUrlCategories()
```


To list all URL Categories within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paUrlCategoriesListUrlCategories("Remote Networks")
```


## Create a URL Category
To create a URL Category in the _Shared_ folder (it defaults to _Shared_)
```python
o = policyObjects.policyObjects(n)

myCustomCategoryURLList1 = { "name": "Allowed_File_Downloads_Sites", "type": "URL List", "list": ["officecdnmac.microsoft.com", "ghcr.io", "pkg-containers.githubusercontent.com", "download.developer.apple.com", "files.pythonhosted.org", "pypi.org"]}
o.paUrlCategoryCreate(myCustomCategoryURLList1)
```

To create a category match
```python
myCustomCategoryMatchList2 = { "name": "myCustomCategory", "type": "Category Match", "list": ["online-storage-and-backup", "gambling", "games"]}
o.paUrlCategoryCreate(myCustomCategoryMatchList2)
```

This will create a URL Category in the "Remote Networks" folder.
```python
o = policyObjects.policyObjects(n)

myCustomCategoryURLList1 = { "name": "Allowed_File_Downloads_Sites", "type": "URL List", "list": ["officecdnmac.microsoft.com", "ghcr.io", "pkg-containers.githubusercontent.com", "download.developer.apple.com", "files.pythonhosted.org", "pypi.org"]}
o.paUrlCategoryCreate(myCustomCategoryURLList1, "Remote Networks")
```

## Edit a URL Category
To edit an existing URL Category in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

myCustomCategoryURLList1 = { "name": "Allowed_File_Downloads_Sites", "type": "URL List", "list": ["newwebsite.com", "newwebsite2.com"]}
o.paUrlCategoriesEdit(myCustomCategoryURLList1, "Remote Networks")
```

## Delete a URL Category
To edit an delete URL Category in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

myCustomCategoryURLList1 = { "name": "Allowed_File_Downloads_Sites" }
o.paUrlCategoriesDelete(myCustomCategoryURLList1, "Remote Networks")
```