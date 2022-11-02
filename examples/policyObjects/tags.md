# Examples on how to work with tags
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

## List all Tags
To list all tags within shared folder (it defaults to _Shared_ folder)
```python
o = policyObjects.policyObjects(n)

o.paTagsListTags()
```


To list all tags within a specific folder, e.g. _Remote Networks_
```python
o = policyObjects.policyObjects(n)

o.paTagsListTags("Remote Networks")
```


## Create a tag
To create a tag in the _Shared_ folder (it defaults to _Shared_)
```python
o = policyObjects.policyObjects(n)

tagObject = { "name": "ExampleTag123", "color": "Azure Blue", "comments": "test 1234 tag object."}
o.paTagCreate(tagObject)
```

This will create a tag in the "Remote Networks" folder.
```python
o = policyObjects.policyObjects(n)

tagObject = { "name": "ExampleTag123", "color": "Azure Blue", "comments": "test 1234 tag object."}
o.paTagCreate(tagObject, "Remote Networks")
```

## Edit a tag
To edit an existing tag in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

tagObject = { "name": "ExampleTag123", "color": "Azure Blue", "comments": "test 1384 tag object."}
o.paTagEdit(tagObject, "Remote Networks")
```

## Delete a Tag
To edit an delete tag in the _Remote Networks_ folder. 

It defaults to _Shared_, so if you want it removed there, just remove the _"Remote Networks"_ argument

```python
o = policyObjects.policyObjects(n)

tagObject = { "name": "ExampleTag" }
o.paTagDelete(tagObject, "Remote Networks")
```