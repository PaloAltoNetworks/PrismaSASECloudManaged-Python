# Examples on how to work with tags
In all examples, it will either return a success or failure when attempting the operation.

## List all Tags
To list all tags within shared folder (it defaults to _Shared_ folder)
```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
n.paTagsListTags()
```


To list all tags within a specific folder, e.g. _Remote Networks_
```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
n.paTagsListTags("Remote Networks")
```


## Create a tag
To create a tag in the _Shared_ folder (it defaults to _Shared_)
```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
tagObject = { "name": "ExampleTag123", "color": "Azure Blue", "comments": "test 1234 tag object."}
n.paTagCreate(tagObject)
```

This will create a tag in the "Remote Networks" folder.
```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()
n = prismaAccess.prismaAccess(p.saseToken)
tagObject = { "name": "ExampleTag123", "color": "Azure Blue", "comments": "test 1234 tag object."}
n.paTagCreate(tagObject, "Remote Networks")
```

## Edit a tag
To edit an existing tag in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()

n = prismaAccess.prismaAccess(p.saseToken)
tagObject = { "name": "ExampleTag123", "color": "Azure Blue", "comments": "test 1384 tag object."}
n.paTagEdit(tagObject, "Remote Networks")
```

## Delete a Tag
To edit an delete tag in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
from auth import saseAuthentication
from access import prismaAccess

p = saseAuthentication.saseAuthentication()
p.prismaAccessAuthLoadToken()

n = prismaAccess.prismaAccess(p.saseToken)
tagObject = { "name": "ExampleTag" }
n.paTagDelete(tagObject, "Remote Networks")
```